# List Languages

This project contains two identical scripts that search the `$PATH`
for installed programming language compilers and interpreters.
The scripts then generate a table listing the detected commands and
their corresponding programming languages.


here is what the output looks like:
```
┌─────────┬─────────────┬───────────┬───────┐
│ (index) │ language    │ command   │ found │
├─────────┼─────────────┼───────────┼───────┤
│ 0       │ Assembly    │ as        │ true  │
│ 1       │ Assembly    │ fasm      │ false │
│ 2       │ Assembly    │ nasm      │ false │
│ 3       │ Assembly    │ yasm      │ false │
│ 4       │ Ada         │ gnat      │ false │
│ 5       │ AWK         │ awk       │ true  │
│ 6       │ Ballerina   │ ballerina │ false │
│ 7       │ BASIC       │ fbc       │ false │
│ 8       │ C           │ gcc       │ true  │
│ 9       │ C           │ clang     │ false │
│ 10      │ C           │ tcc       │ false │
│ 11      │ C           │ sdcc      │ false │
│ 12      │ C++         │ gcc       │ true  │
│ 13      │ C++         │ clang     │ false │
│ 14      │ Objective-C │ gcc       │ true  │
│ 15      │ Objective-C │ clang     │ false │
│ 16      │ C#          │ mcs       │ false │
│ 17      │ Crystal     │ crystal   │ false │
│ 18      │ D           │ dmd       │ false │
│ 19      │ Dart        │ dart      │ false │
│ 20      │ Erlang      │ erl       │ false │
│ 21      │ Elixer      │ elixer    │ false │
│ 22      │ Forth       │ gforth    │ false │
│ 23      │ Fortran     │ gfortran  │ false │
│ 24      │ Go          │ go        │ true  │
│ 25      │ Go          │ gccgo     │ false │
│ 26      │ Go          │ tinygo    │ false │
│ 27      │ Java        │ javac     │ false │
│ 28      │ Groovy      │ groovy    │ false │
│ 29      │ GDL         │ gdl       │ false │
│ 30      │ Haskell     │ ghc       │ false │
│ 31      │ JavaScript  │ node      │ true  │
│ 32      │ JavaScript  │ bun       │ true  │
│ 33      │ JavaScript  │ deno      │ false │
│ 34      │ TypeScript  │ ts-node   │ false │
│ 35      │ TypeScript  │ bun       │ true  │
│ 36      │ TypeScript  │ deno      │ false │
│ 37      │ Julia       │ julia     │ false │
│ 38      │ Kotlin      │ kotlinc   │ false │
│ 39      │ Clojure     │ clojure   │ false │
│ 40      │ Common Lisp │ sbcl      │ false │
│ 41      │ Common Lisp │ ecl       │ false │
│ 42      │ Emacs Lisp  │ emacs     │ false │
│ 43      │ Scheme      │ bigloo    │ false │
│ 44      │ Scheme      │ chicken   │ false │
│ 45      │ Scheme      │ gosh      │ false │
│ 46      │ Scheme      │ guile     │ true  │
│ 47      │ Scheme      │ racket    │ false │
│ 48      │ Lua         │ lua       │ true  │
│ 49      │ Lua         │ luajit    │ true  │
│ 50      │ Standard ML │ sml       │ false │
│ 51      │ Standard ML │ mlton     │ false │
│ 52      │ Standard ML │ poly      │ false │
│ 53      │ Ocaml       │ ocaml     │ false │
│ 54      │ Nim         │ nim       │ false │
│ 55      │ Octave      │ octave    │ false │
│ 56      │ Pascal      │ fpc       │ false │
│ 57      │ Perl        │ perl      │ true  │
│ 58      │ PHP         │ php       │ false │
│ 59      │ Python      │ python    │ true  │
│ 60      │ Python      │ pypy      │ false │
│ 61      │ R           │ R         │ false │
│ 62      │ Ruby        │ ruby      │ false │
│ 63      │ Rust        │ rustc     │ true  │
│ 64      │ Rust        │ rustup    │ true  │
│ 65      │ Scala       │ scala     │ false │
│ 66      │ Swift       │ swift     │ false │
│ 67      │ Tcl         │ tclsh     │ false │
│ 68      │ Vala        │ valac     │ false │
│ 69      │ Zig         │ zig       │ false │
└─────────┴─────────────┴───────────┴───────┘
```
