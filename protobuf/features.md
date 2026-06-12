Feature Settings for Editions | Protocol Buffers Documentation

View page source

Edit this page

Create child page

Create documentation issue

Create project issue

Feature Settings for Editions

Protobuf Editions features and how they affect protobuf behavior.

This topic provides an overview of the features that are included in the
released edition versions. Subsequent editions’ features will be added to this
topic. We announce new editions in

the News section

Before configuring feature settings in your new schema definition content, make
sure you understand why you are using them. Avoid

cargo-culting

with
features.

Prototiller

Prototiller is a command-line tool that updates proto schema configuration files
between syntax versions and editions. It hasn’t been released yet, but is
referenced throughout this topic.

Features

The following sections include all of the behaviors that are configurable using
features in editions.

Preserving proto2 or proto3 Behavior

shows
how to override the default behaviors so that your proto definition files act
like proto2 or proto3 files. For more information on how editions and features
work together to set behavior, see

Protobuf Editions Overview

Feature settings apply at different levels:

File-level:

These settings apply to all elements (messages, fields, enums,
and so on) that don’t have an overriding setting.

Non-nested:

Messages, enums, and services can override settings made at the
file level. They apply to everything within them (message fields, enum values)
that aren’t overridden, but don’t apply to other parallel messages and enums.

Nested:

Oneofs, messages, and enums can override settings from the message
they’re nested in.

Lowest-level:

Fields, extensions, enum values, extension ranges, and methods
are the lowest level at which you can override settings.

Each of the following sections has a comment that states what scope the feature
can be applied to. The following sample shows a mock feature applied to each
scope:

edition

"2024"

// File-level scope definition

option

features.bar

enum

// Enum (non-nested scope) definition

option

features.bar

message

Corge

// Message (non-nested scope) definition

option

features.bar

QUUX

message

Garply

// Message (nested scope) definition

option

features.bar

WALDO

string

// Field (lowest-level scope) definition

features.bar

GRAULT

In this example, the setting “

GRAULT"

in the lowest-level scope feature
definition overrides the non-nested-scope “

QUUX

” setting. And within the
Garply message, “

WALDO

” overrides “

QUUX

features.default_symbol_visibility

This feature enables setting the default visibility for messages and enums,
making them available or unavailable when imported by other protos. Use of this
feature will reduce dead symbols in order to create smaller binaries.

In addition to setting the defaults for the entire file, you can use the

local

export

keywords to set per-field behavior. Read more about this at

export

local

Keywords

Values available:

EXPORT_ALL

: This is the default prior to Edition 2024. All messages and
enums are exported by default.

EXPORT_TOP_LEVEL

: All top-level symbols default to export; nested default
to local.

LOCAL_ALL

: All symbols default to local.

STRICT

: All symbols local by default. Nested types cannot be exported,
except for a special-case caveat for

message { enum {} reserved 1 to max; }

. This will become the default in a future edition.

Applicable to the following scope:

file

Added in:

Edition 2024

Default behavior per syntax/edition:

Syntax/edition

Default

2024

EXPORT_TOP_LEVEL

2023

EXPORT_ALL

proto3

EXPORT_ALL

proto2

EXPORT_ALL

Note:

Feature settings on different schema elements

have different scopes

The following sample shows how you can apply the feature to elements in your
proto schema definition files:

// foo.proto

edition

"2024"

// Symbol visibility defaults to EXPORT_TOP_LEVEL. Setting

// default_symbol_visibility overrides these defaults

option

features.default_symbol_visibility

LOCAL_ALL

// Top-level symbols are exported by default in Edition 2024; applying the local

// keyword overrides this

export

message

LocalMessage

int32

// Nested symbols are local by default in Edition 2024; applying the export

// keyword overrides this

enum

ExportedNestedEnum

UNKNOWN_EXPORTED_NESTED_ENUM_VALUE

// bar.proto

edition

"2024"

import

"foo.proto"

message

ImportedMessage

// The following is valid because the imported message explicitly overrides

// the visibility setting in foo.proto

LocalMessage

// The following is not valid because default_symbol_visibility is set to

// `LOCAL_ALL`

// LocalMessage.ExportedNestedEnum qux = 2;

features.enforce_naming_style

Introduced in Edition 2024, this feature enables strict naming style enforcement
as defined in

the style guide

to ensure
protos are round-trippable by default with a feature value to opt-out to use
legacy naming style.

Values available:

STYLE2024

: Enforces strict adherence to the style guide for naming.

STYLE_LEGACY

: Applies the pre-Edition 2024 level of style guide
enforcement.

Applicable to the following scopes:

file, extension range, message, field,
oneof, enum, enum value, service, method

Added in:

Edition 2024

Default behavior per syntax/edition:

Syntax/edition

Default

2024

STYLE2024

2023

STYLE_LEGACY

proto3

STYLE_LEGACY

proto2

STYLE_LEGACY

Note:

Feature settings on different schema elements

have different scopes

The following code sample shows an Edition 2023 file:

Edition 2023 defaults to

STYLE_LEGACY

, so a non-conformant field name is fine:

edition

"2023"

message

// A non-conforming field name is not a problem

int64

bar_1

Edition 2024 defaults to

STYLE2024

, so an override is needed to keep the
non-conformant field name:

edition

"2024"

// To keep the non-conformant field name, override the STYLE2024 setting

option

features.enforce_naming_style

STYLE_LEGACY

message

int64

bar_1

features.enum_type

This feature sets the behavior for how enum values that aren’t contained within
the defined set are handled. See

Enum Behavior

for more
information on open and closed enums.

This feature doesn’t impact proto3 files, so this section doesn’t have a before
and after of a proto3 file.

Values available:

CLOSED:

Closed enums store enum values that are out of range in the
unknown field set.

OPEN:

Open enums parse out of range values into their fields directly.

Applicable to the following scopes:

file, enum

Added in:

Edition 2023

Default behavior per syntax/edition:

Syntax/edition

Default

2024

OPEN

2023

OPEN

proto3

OPEN

proto2

CLOSED

Note:

Feature settings on different schema elements

have different scopes

The following code sample shows a proto2 file:

syntax

"proto2"

enum

After running

Prototiller

, the equivalent code might look like
this:

edition

"2024"

enum

// Setting the enum_type feature overrides the default OPEN enum

option

features.enum_type

CLOSED

features.field_presence

This feature sets the behavior for tracking field presence, or the notion of
whether a protobuf field has a value.

Values available:

LEGACY_REQUIRED

: The field is required for parsing and serialization.
Any explicitly-set value is
serialized onto the wire (even if it is the same as the default value).

EXPLICIT

: The field has explicit presence tracking. Any explicitly-set
value is serialized onto the wire (even if it is the same as the default
value). For singular primitive fields,

has_*

functions are generated for
fields set to

EXPLICIT

IMPLICIT

: The field has no presence tracking. The default value is not
serialized onto the wire (even if it is explicitly set).

has_*

functions
are not generated for fields set to

IMPLICIT

Applicable to the following scopes:

file, field

Added in:

Edition 2023

Default behavior per syntax/edition:

Syntax/edition

Default

2024

EXPLICIT

2023

EXPLICIT

proto3

IMPLICIT

proto2

EXPLICIT

* proto3 is

IMPLICIT

unless the field has the

optional

label, in which case
it behaves like

EXPLICIT

. See

Presence in Proto3 APIs

for more information.

Note:

Feature settings on different schema elements

have different scopes

The following code sample shows a proto2 file:

syntax

"proto2"

message

required

int32

optional

int32

repeated

int32

After running Prototiller, the equivalent code might look like this:

edition

"2024"

message

// Setting the field_presence feature retains the proto2 required behavior

int32

features.field_presence

LEGACY_REQUIRED

int32

repeated

int32

The following shows a proto3 file:

syntax

"proto3"

message

int32

optional

int32

repeated

int32

After running Prototiller, the equivalent code might look like this:

edition

"2024"