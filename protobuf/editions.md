Language Guide (editions) | Protocol Buffers Documentation

View page source

Edit this page

Create child page

Create documentation issue

Create project issue

Language Guide (editions)

Covers how to use the editions revisions of the Protocol Buffers language in your project.

This guide describes how to use the protocol buffer language to structure your
protocol buffer data, including

.proto

file syntax and how to generate data
access classes from your

.proto

files. It covers

edition 2023

edition
2024

of the protocol buffers language. For information about how editions
differ from proto2 and proto3 conceptually, see

Protobuf Editions Overview

For information on the

proto2

syntax, see the

Proto2 Language Guide

For information on

proto3

syntax, see the

Proto3 Language Guide

This is a reference guide – for a step by step example that uses many of the
features described in this document, see the

tutorial

for your chosen language.

Defining A Message Type

First let’s look at a very simple example. Let’s say you want to define a search
request message format, where each search request has a query string, the
particular page of results you are interested in, and a number of results per
page. Here’s the

.proto

file you use to define the message type.

edition

"2023"

message

SearchRequest

string

query

int32

page_number

int32

results_per_page

The first line of the file specifies that you’re using edition 2023 of the
protobuf language spec.

edition

syntax

for proto2/proto3) must be the first
non-empty, non-comment line of the file.

If no

edition

syntax

is specified, the protocol buffer compiler
will assume you are using

proto2

SearchRequest

message definition specifies three fields (name/value
pairs), one for each piece of data that you want to include in this type of
message. Each field has a name and a type.

Specifying Field Types

In the earlier example, all the fields are

scalar types

: two integers
(

page_number

results_per_page

) and a string (

query

). You can also
specify

enumerations

and composite types like other message types for
your field.

Assigning Field Numbers

You must give each field in your message definition a number between

536,870,911

with the following restrictions:

The given number

must be unique

among all fields for that message.

Field numbers

19,000

19,999

are reserved for the Protocol Buffers
implementation. The protocol buffer compiler will complain if you use one of
these reserved field numbers in your message.

You cannot use any previously

reserved

field numbers or
any field numbers that have been allocated to

extensions

This number

cannot be changed once your message type is in use

because it
identifies the field in the

message wire format

.
“Changing” a field number is equivalent to deleting that field and creating a
new field with the same type but a new number. See

Deleting Fields

for how to do this properly.

Field numbers

should never be reused

. Never take a field number out of the

reserved

list for reuse with a new field definition. See

Consequences of Reusing Field Numbers

You should use the field numbers 1 through 15 for the most-frequently-set
fields. Lower field number values take less space in the wire format. For
example, field numbers in the range 1 through 15 take one byte to encode. Field
numbers in the range 16 through 2047 take two bytes. You can find out more about
this in

Protocol Buffer Encoding

Consequences of Reusing Field Numbers

Reusing a field number makes decoding wire-format messages ambiguous.

The protobuf wire format is lean and doesn’t provide a way to detect fields
encoded using one definition and decoded using another.

Encoding a field using one definition and then decoding that same field with a
different definition can lead to:

Developer time lost to debugging

A parse/merge error (best case scenario)

Leaked PII/SPII

Data corruption

Common causes of field number reuse:

renumbering fields (sometimes done to achieve a more aesthetically pleasing
number order for fields). Renumbering effectively deletes and re-adds all
the fields involved in the renumbering, resulting in incompatible
wire-format changes.

deleting a field and not

reserving

the number to prevent
future reuse.

This has been a very easy mistake to make with

extension fields

for several reasons.

Extension Declarations

provide a mechanism for reserving extension fields.

The field number is limited to 29 bits rather than 32 bits because three bits
are used to specify the field’s wire format. For more on this, see the

Encoding topic

Specifying Field Cardinality

Message fields can be one of the following:

Singular

A singular field has no explicit cardinality label. It has two possible
states:

the field is set, and contains a value that was explicitly set or parsed
from the wire. It will be serialized to the wire.

the field is unset, and will return the default value. It will not be
serialized to the wire.

You can check to see if the value was explicitly set.

Proto3

implicit

fields that have been migrated to editions will use the

field_presence

feature set to the

IMPLICIT

value.

Proto2

required

fields that have been migrated to editions will also use
the

field_presence

feature, but set to

LEGACY_REQUIRED

repeated

: this field type can be repeated zero or more times in a
well-formed message. The order of the repeated values will be preserved.

: this is a paired key/value field type. See

Maps

for more on
this field type.

Repeated Fields are Packed by Default

In proto editions,

repeated

fields of scalar numeric types use

packed

encoding by default.

You can find out more about

packed

encoding in

Protocol Buffer Encoding

Well-formed Messages

The term “well-formed,” when applied to protobuf messages, refers to the bytes
serialized/deserialized. The protoc parser validates that a given proto
definition file is parseable.

Singular fields can appear more than once in wire-format bytes. The parser will
accept the input, but only the last instance of that field will be accessible
through the generated bindings. See

Last One Wins

for more on this topic.

Adding More Message Types

Multiple message types can be defined in a single

.proto

file. This is useful
if you are defining multiple related messages – so, for example, if you wanted
to define the reply message format that corresponds to your

SearchResponse

message type, you could add it to the same

.proto

message

SearchRequest

string

query

int32

page_number

int32

results_per_page

message

SearchResponse

Combining Messages leads to bloat

While multiple message types (such as
message, enum, and service) can be defined in a single

.proto

file, it can
also lead to dependency bloat when large numbers of messages with varying
dependencies are defined in a single file. It’s recommended to include as few
message types per

.proto

file as possible.

Adding Comments

To add comments to your

.proto

files:

Prefer C/C++/Java line-end-style comments ‘//’ on the line before the .proto
code element

C-style inline/multi-line comments

/* ... */

are also accepted.

When using multi-line comments, a margin line of ‘*’ is preferred.

* SearchRequest represents a search query, with pagination options to

* indicate which results to include in the response.

message

SearchRequest

string

query

// Which page number do we want?

int32

page_number

// Number of results to return per page.

int32

results_per_page

Deleting Fields

Deleting fields can cause serious problems if not done properly.

When you no longer need a field and all references have been deleted from client
code, you may delete the field definition from the message. However, you

must

reserve the deleted field number

. If you do not
reserve the field number, it is possible for a developer to reuse that number in
the future.

You should also reserve the field name to allow JSON and TextFormat encodings of
your message to continue to parse.

Reserved Field Numbers

If you

update

a message type by entirely deleting a field, or
commenting it out, future developers can reuse the field number when making
their own updates to the type. This can cause severe issues, as described in

Consequences of Reusing Field Numbers

. To make sure this
doesn’t happen, add your deleted field number to the

reserved

list.

The protoc compiler will generate error messages if any future developers try to
use these reserved field numbers.

message

reserved

Reserved field number ranges are inclusive (

9 to 11

is the same as

9, 10, 11

Reserved Field Names

Reusing an old field name later is generally safe, except when using TextProto
or JSON encodings where the field name is serialized. To avoid this risk, you
can add the deleted field name to the

reserved

list.

Reserved names affect only the protoc compiler behavior and not runtime
behavior, with one exception: TextProto implementations may discard unknown
fields (without raising an error like with other unknown fields) with reserved
names at parse time (only the C++ and Go implementations do so today). Runtime
JSON parsing is not affected by reserved names.

message

reserved

reserved

Note that you can’t mix field names and field numbers in the same

reserved

statement.

What’s Generated from Your

.proto

When you run the

protocol buffer compiler

on a

.proto

, the
compiler generates the code in your chosen language you’ll need to work with the
message types you’ve described in the file, including getting and setting field
values, serializing your messages to an output stream, and parsing your messages
from an input stream.

, the compiler generates a

file from each

.proto

, with a class for each message type described in your file.

Java

, the compiler generates a

.java

file with a class for each
message type, as well as a special

Builder

class for creating message
class instances.

Kotlin

, in addition to the Java generated code, the compiler
generates a

file for each message type with an improved Kotlin API.
This includes a DSL that simplifies creating message instances, a nullable
field accessor, and a copy function.

Python

is a little different — the Python compiler generates a module
with a static descriptor of each message type in your

.proto

, which is
then used with a

metaclass

to create the necessary Python data access
class at runtime.

, the compiler generates a

.pb.go

file with a type for each
message type in your file.

Ruby

, the compiler generates a

file with a Ruby module
containing your message types.

Objective-C

, the compiler generates a

pbobjc.h

pbobjc.m

file
from each

.proto

, with a class for each message type described in your
file.

, the compiler generates a

file from each

.proto

, with a
class for each message type described in your file.

, the compiler generates a

.php

message file for each message
type described in your file, and a

.php

metadata file for each

.proto

file you compile. The metadata file is used to load the valid message types
into the descriptor pool.

Dart

, the compiler generates a

.pb.dart

file with a class for each
message type in your file.

You can find out more about using the APIs for each language by following the
tutorial for your chosen language. For even more API
details, see the relevant

API reference

Scalar Value Types

A scalar message field can have one of the following types – the table shows the
type specified in the

.proto

file, and the corresponding type in the
automatically generated class:

Proto Type

Notes

double

float

int32

Uses variable-length encoding. Inefficient for encoding negative
numbers – if your field is likely to have negative values, use sint32
instead.

int64

Uses variable-length encoding. Inefficient for encoding negative
numbers – if your field is likely to have negative values, use sint64
instead.

uint32