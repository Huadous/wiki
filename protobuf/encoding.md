Encoding | Protocol Buffers Documentation

View page source

Edit this page

Create child page

Create documentation issue

Create project issue

Encoding

Explains how Protocol Buffers encodes data to files or to the wire.

This document describes the protocol buffer

wire format

, which defines the
details of how your message is sent on the wire and how much space it consumes
on disk. You probably don’t need to understand this to use protocol buffers in
your application, but it’s useful information for doing optimizations.

If you already know the concepts but want a reference, skip to the

Condensed reference card

section.

Protoscope

is a very simple
language for describing snippets of the low-level wire format, which we’ll use
to provide a visual reference for the encoding of various messages. Protoscope’s
syntax consists of a sequence of

tokens

that each encode down to a specific
byte sequence.

For example, backticks denote a raw hex literal, like

`70726f746f6275660a`

. This encodes into the exact bytes denoted as hex in the literal. Quotes
denote UTF-8 strings, like

"Hello, Protobuf!"

. This literal is synonymous with

`48656c6c6f2c2050726f746f62756621`

(which, if you observe closely, is
composed of ASCII bytes). We’ll introduce more of the Protoscope language as we
discuss aspects of the wire format.

The Protoscope tool can also dump encoded protocol buffers as text. See

https://github.com/protocolbuffers/protoscope/tree/main/testdata

for examples.

All examples in this topic assume that you are using Edition 2023 or later.

A Simple Message

Let’s say you have the following very simple message definition:

message

Test1

int32

In an application, you create a

Test1

message and set

to 150. You then
serialize the message to an output stream. If you were able to examine the
encoded message, you’d see three bytes:

So far, so small and numeric – but what does it mean? If you use the Protoscope
tool to dump those bytes, you’d get something like

1: 150

. How does it know
this is the contents of the message?

Base 128 Varints

Variable-width integers, or

varints

, are at the core of the wire format. They
allow encoding unsigned 64-bit integers using anywhere between one and ten
bytes, with small values using fewer bytes.

Each byte in the varint has a

continuation bit

that indicates if the byte that
follows it is part of the varint. This is the

most significant bit

(MSB) of
the byte (sometimes also called the

sign bit

). The lower 7 bits are a payload;
the resulting integer is built by appending together the 7-bit payloads of its
constituent bytes.

So, for example, here is the number 1, encoded as

`01`

– it’s a single
byte, so the MSB is not set:

0000

0001

And here is 150, encoded as

`9601`

– this is a bit more complicated:

10010110

00000001

How do you figure out that this is 150? First you drop the MSB from each byte,
as this is just there to tell us whether we’ve reached the end of the number (as
you can see, it’s set in the first byte as there is more than one byte in the
varint). These 7-bit payloads are in little-endian order. Convert to big-endian
order, concatenate, and interpret as an unsigned 64-bit integer:

10010110

00000001

// Original inputs.

0010110

0000001

// Drop continuation bits.

0000001

0010110

// Convert to big-endian.

00000010010110

// Concatenate.

// Interpret as an unsigned 64-bit integer.

Because varints are so crucial to protocol buffers, in protoscope syntax, we
refer to them as plain integers.

is the same as

`9601`

Message Structure

A protocol buffer message is a series of key-value pairs. The binary version of
a message just uses the field’s number as the key – the name and declared type
for each field can only be determined on the decoding end by referencing the
message type’s definition (i.e. the

.proto

file). Protoscope does not have
access to this information, so it can only provide the field numbers.

When a message is encoded, each key-value pair is turned into a

record

consisting of the field number, a wire type and a payload. The wire type tells
the parser how big the payload after it is. This allows old parsers to skip over
new fields they don’t understand. This type of scheme is sometimes called

Tag-Length-Value

,
or TLV.

There are six wire types:

VARINT

SGROUP

EGROUP

, and

Name

Used For

VARINT

int32, int64, uint32, uint64, sint32, sint64, bool, enum

fixed64, sfixed64, double

string, bytes, embedded messages, packed repeated fields

SGROUP

group start (deprecated)

EGROUP

group end (deprecated)

fixed32, sfixed32, float

The “tag” of a record is encoded as a varint formed from the field number and
the wire type via the formula

(field_number << 3) | wire_type

. In other words,
after decoding the varint representing a field, the low 3 bits tell us the wire
type, and the rest of the integer tells us the field number.

Now let’s look at our simple example again. You now know that the first number
in the stream is always a varint key, and here it’s

`08`

, or (dropping the
MSB):

1000

You take the last three bits to get the wire type (0) and then right-shift by
three to get the field number (1). Protoscope represents a tag as an integer
followed by a colon and the wire type, so we can write the above bytes as

1:VARINT

Because the wire type is 0, or

VARINT

, we know that we need to decode a varint
to get the payload. As we saw above, the bytes

`9601`

varint-decode to
150, giving us our record. We can write it in Protoscope as

1:VARINT 150

Protoscope can infer the type for a tag if there is whitespace after the

. It
does so by looking ahead at the next token and guessing what you meant (the
rules are documented in detail in

Protoscope’s language.txt

).
For example, in

1: 150

, there is a varint immediately after the untyped tag,
so Protoscope infers its type to be

VARINT

. If you wrote

2: {}

, it would see
the

and guess

; if you wrote

3: 5i32

it would guess

, and so on.

More Integer Types

Bools and Enums

Bools and enums are both encoded as if they were

int32

s. Bools, in particular,
always encode as either

`00`

`01`

. In Protoscope,

false

true

are aliases for these byte strings.

Signed Integers

As you saw in the previous section, all the protocol buffer types associated
with wire type 0 are encoded as varints. However, varints are unsigned, so the
different signed types,

sint32

sint64

int32

int64

, encode
negative integers differently.

intN

types encode negative numbers as two’s complement, which means that,
as unsigned, 64-bit integers, they have their highest bit set. As a result, this
means that

all ten bytes

must be used. For example,

is converted by
protoscope into

11111110

11111111

11111111

11111111

11111111

11111111

11111111

11111111

11111111

00000001

This is the

two’s complement

of 2, defined in unsigned arithmetic as

~0 - 2 + 1

, where

is the all-ones 64-bit integer. It is a useful exercise to
understand why this produces so many ones.

sintN

uses the “ZigZag” encoding instead of two’s complement to encode
negative integers. Positive integers

are encoded as

2 * p

(the even
numbers), while negative integers

are encoded as

2 * |n| - 1

(the odd
numbers). The encoding thus “zig-zags” between positive and negative numbers.
For example:

Signed Original

Encoded As

0x7fffffff

0xfffffffe

-0x80000000

0xffffffff

In other words, each value

is encoded using

(n << 1) ^ (n >> 31)

sint32

s, or

(n << 1) ^ (n >> 63)

for the 64-bit version.

When the

sint32

sint64

is parsed, its value is decoded back to the
original, signed version.

In protoscope, suffixing an integer with a

will make it encode as ZigZag.
For example,

-500z

is the same as the varint

Non-varint Numbers

Non-varint numeric types are simple.

double

fixed64

have wire type

, which tells the parser to expect a fixed eight-byte lump of data.

double

values are encoded in IEEE 754 double-precision format. We can specify
a

double

record by writing

5: 25.4

, or a

fixed64

record with

6: 200i64

Similarly

float

fixed32

have wire type

, which tells it to expect
four bytes instead.

float

values are encoded in IEEE 754 single-precision
format. The syntax for these consists of adding an

suffix.

25.4i32

will
emit four bytes, as will

200i32

. Tag types are inferred as

Length-Delimited Records

Length prefixes

are another major concept in the wire format. The

wire
type has a dynamic length, specified by a varint immediately after the tag,
which is followed by the payload as usual.

Consider this message schema:

message

Test2

string

A record for the field

is a string, and strings are

-encoded. If we set

"testing"

, we encoded as a

record with field number 2 containing
the ASCII string

"testing"

. The result is

`120774657374696e67`

. Breaking
up the bytes,

we see that the tag,

`12`

, is

00010 010

, or

2:LEN

. The byte that
follows is the int32 varint

, and the next seven bytes are the UTF-8
encoding of

"testing"

. The int32 varint means that the max length of a string
is 2GB.

In Protoscope, this is written as

2:LEN 7 "testing"

. However, it can be
inconvenient to repeat the length of the string (which, in Protoscope text, is
already quote-delimited). Wrapping Protoscope content in braces will generate a
length prefix for it:

{"testing"}

is a shorthand for

7 "testing"

is
always inferred by fields to be a

record, so we can write this record
simply as

2: {"testing"}

bytes

fields are encoded in the same way.

Submessages

Submessage fields also use the

wire type. Here’s a message definition with
an embedded message of our original example message,

Test1

message

Test3

Test1

Test1

field (i.e.,

Test3

field) is set to 150, we get

``1a03089601``

. Breaking it up:

The last three bytes (in

) are exactly the same ones from our

very first example

. These bytes are preceded by a

-typed tag,
and a length of 3, exactly the same way as strings are encoded.

In Protoscope, submessages are quite succinct.

``1a03089601``

can be written
as

3: {1: 150}

Missing Elements

Missing fields are easy to encode: we just leave out the record if
it’s not present. This means that “huge” protos with only a few fields set are
quite sparse.

Repeated Elements

Starting in Edition 2023,

repeated

fields of a primitive type
(any

scalar type

that is not

string

bytes

) are