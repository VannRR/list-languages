import os
import sys

LANGUAGES = [
    {"language": "Assembly", "command": "as", "found": False},
    {"language": "Assembly", "command": "fasm", "found": False},
    {"language": "Assembly", "command": "nasm", "found": False},
    {"language": "Assembly", "command": "yasm", "found": False},
    {"language": "Ada", "command": "gnat", "found": False},
    {"language": "AWK", "command": "awk", "found": False},
    {"language": "Ballerina", "command": "ballerina", "found": False},
    {"language": "BASIC", "command": "fbc", "found": False},
    {"language": "C", "command": "gcc", "found": False},
    {"language": "C", "command": "clang", "found": False},
    {"language": "C", "command": "tcc", "found": False},
    {"language": "C", "command": "sdcc", "found": False},
    {"language": "C++", "command": "gcc", "found": False},
    {"language": "C++", "command": "clang", "found": False},
    {"language": "Objective-C", "command": "gcc", "found": False},
    {"language": "Objective-C", "command": "clang", "found": False},
    {"language": "C#", "command": "mcs", "found": False},
    {"language": "Crystal", "command": "crystal", "found": False},
    {"language": "D", "command": "dmd", "found": False},
    {"language": "Dart", "command": "dart", "found": False},
    {"language": "Erlang", "command": "erl", "found": False},
    {"language": "Elixer", "command": "elixer", "found": False},
    {"language": "Forth", "command": "gforth", "found": False},
    {"language": "Fortran", "command": "gfortran", "found": False},
    {"language": "Go", "command": "go", "found": False},
    {"language": "Go", "command": "gccgo", "found": False},
    {"language": "Go", "command": "tinygo", "found": False},
    {"language": "Java", "command": "javac", "found": False},
    {"language": "Groovy", "command": "groovy", "found": False},
    {"language": "GDL", "command": "gdl", "found": False},
    {"language": "Haskell", "command": "ghc", "found": False},
    {"language": "JavaScript", "command": "node", "found": False},
    {"language": "JavaScript", "command": "bun", "found": False},
    {"language": "JavaScript", "command": "deno", "found": False},
    {"language": "TypeScript", "command": "ts-node", "found": False},
    {"language": "TypeScript", "command": "bun", "found": False},
    {"language": "TypeScript", "command": "deno", "found": False},
    {"language": "Julia", "command": "julia", "found": False},
    {"language": "Kotlin", "command": "kotlinc", "found": False},
    {"language": "Clojure", "command": "clojure", "found": False},
    {"language": "Common Lisp", "command": "sbcl", "found": False},
    {"language": "Common Lisp", "command": "ecl", "found": False},
    {"language": "Emacs Lisp", "command": "emacs", "found": False},
    {"language": "Scheme", "command": "bigloo", "found": False},
    {"language": "Scheme", "command": "chicken", "found": False},
    {"language": "Scheme", "command": "gosh", "found": False},
    {"language": "Scheme", "command": "guile", "found": False},
    {"language": "Scheme", "command": "racket", "found": False},
    {"language": "Lua", "command": "lua", "found": False},
    {"language": "Lua", "command": "luajit", "found": False},
    {"language": "Standard ML", "command": "sml", "found": False},
    {"language": "Standard ML", "command": "mlton", "found": False},
    {"language": "Standard ML", "command": "poly", "found": False},
    {"language": "Ocaml", "command": "ocaml", "found": False},
    {"language": "Nim", "command": "nim", "found": False},
    {"language": "Octave", "command": "octave", "found": False},
    {"language": "Pascal", "command": "fpc", "found": False},
    {"language": "Perl", "command": "perl", "found": False},
    {"language": "PHP", "command": "php", "found": False},
    {"language": "Python", "command": "python", "found": False},
    {"language": "Python", "command": "pypy", "found": False},
    {"language": "R", "command": "R", "found": False},
    {"language": "Ruby", "command": "ruby", "found": False},
    {"language": "Rust", "command": "rustc", "found": False},
    {"language": "Rust", "command": "rustup", "found": False},
    {"language": "Scala", "command": "scala", "found": False},
    {"language": "Swift", "command": "swift", "found": False},
    {"language": "Tcl", "command": "tclsh", "found": False},
    {"language": "Vala", "command": "valac", "found": False},
    {"language": "Zig", "command": "zig", "found": False},
]

def list_files(dir):
    try:
        files = os.listdir(dir)
        return files
    except Exception as err:
        print(f"Error reading directory {dir}: {err}", file=sys.stderr)
        sys.exit(1)

def get_all_files_in_path():
    if os.getenv("PATH") is None:
        print("PATH environment variable not found", file=sys.stderr)
        sys.exit(1)

    path_dirs = {dir for dir in os.getenv("PATH").split(os.pathsep) if dir and "/sbin" not in dir}
    all_files = set()

    for dir in path_dirs:
        files = list_files(dir)
        all_files.update(files)

    return all_files


def print_languages(languages):
    headers = ["(index)", "language", "command", "found"]
    max_lens = [max(len(str(i)) for i in range(len(languages))),
                max(len(lang['language']) for lang in languages),
                max(len(lang['command']) for lang in languages),
                len("found")]

    max_lens = [max(max_len, len(header)) for max_len, header in zip(max_lens, headers)]

    def format_row(*args):
        return "│ " + " │ ".join(f"{arg:<{max_len}}" for arg, max_len in zip(args, max_lens)) + " │"

    header = format_row(*headers)
    separator = "├" + "┼".join("─" * (max_len + 2) for max_len in max_lens) + "┤"
    footer = "└" + "┴".join("─" * (max_len + 2) for max_len in max_lens) + "┘"

    rows = [format_row(index, lang['language'], lang['command'], str(lang['found']).lower()) for index, lang in enumerate(languages)]

    table = ["┌" + "┬".join("─" * (max_len + 2) for max_len in max_lens) + "┐", header, separator] + rows + [footer]

    print("\n".join(table))


def main():
    files = get_all_files_in_path()

    for entry in LANGUAGES:
        if entry["command"] in files:
            entry["found"] = True

    print_languages(LANGUAGES)

if __name__ == "__main__":
    main()
