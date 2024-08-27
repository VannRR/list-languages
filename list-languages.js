import fs from "fs";
import path from "path";

const LANGUAGES = [
    {language: "Assembly", command: "as", found: false},
    {language: "Assembly", command: "fasm", found: false},
    {language: "Assembly", command: "nasm", found: false},
    {language: "Assembly", command: "yasm", found: false},
    {language: "Ada", command: "gnat", found: false},
    {language: "AWK", command: "awk", found: false},
    {language: "Ballerina", command: "ballerina", found: false},
    {language: "BASIC", command: "fbc", found: false},
    {language: "C", command: "gcc", found: false},
    {language: "C", command: "clang", found: false},
    {language: "C", command: "tcc", found: false},
    {language: "C", command: "sdcc", found: false},
    {language: "C++", command: "gcc", found: false},
    {language: "C++", command: "clang", found: false},
    {language: "Objective-C", command: "gcc", found: false},
    {language: "Objective-C", command: "clang", found: false},
    {language: "C#", command: "mcs", found: false},
    {language: "Crystal", command: "crystal", found: false},
    {language: "D", command: "dmd", found: false},
    {language: "Dart", command: "dart", found: false},
    {language: "Erlang", command: "erl", found: false},
    {language: "Elixer", command: "elixer", found: false},
    {language: "Forth", command: "gforth", found: false},
    {language: "Fortran", command: "gfortran", found: false},
    {language: "Go", command: "go", found: false},
    {language: "Go", command: "gccgo", found: false},
    {language: "Go", command: "tinygo", found: false},
    {language: "Java", command: "javac", found: false},
    {language: "Groovy", command: "groovy", found: false},
    {language: "GDL", command: "gdl", found: false},
    {language: "Haskell", command: "ghc", found: false},
    {language: "JavaScript", command: "node", found: false},
    {language: "JavaScript", command: "bun", found: false},
    {language: "JavaScript", command: "deno", found: false},
    {language: "TypeScript", command: "ts-node", found: false},
    {language: "TypeScript", command: "bun", found: false},
    {language: "TypeScript", command: "deno", found: false},
    {language: "Julia", command: "julia", found: false},
    {language: "Kotlin", command: "kotlinc", found: false},
    {language: "Clojure", command: "clojure", found: false},
    {language: "Common Lisp", command: "sbcl", found: false},
    {language: "Common Lisp", command: "ecl", found: false},
    {language: "Emacs Lisp", command: "emacs", found: false},
    {language: "Scheme", command: "bigloo", found: false},
    {language: "Scheme", command: "chicken", found: false},
    {language: "Scheme", command: "gosh", found: false},
    {language: "Scheme", command: "guile", found: false},
    {language: "Scheme", command: "racket", found: false},
    {language: "Lua", command: "lua", found: false},
    {language: "Lua", command: "luajit", found: false},
    {language: "Standard ML", command: "sml", found: false},
    {language: "Standard ML", command: "mlton", found: false},
    {language: "Standard ML", command: "poly", found: false},
    {language: "Ocaml", command: "ocaml", found: false},
    {language: "Nim", command: "nim", found: false},
    {language: "Octave", command: "octave", found: false},
    {language: "Pascal", command: "fpc", found: false},
    {language: "Perl", command: "perl", found: false},
    {language: "PHP", command: "php", found: false},
    {language: "Python", command: "python", found: false},
    {language: "Python", command: "pypy", found: false},
    {language: "R", command: "R", found: false},
    {language: "Ruby", command: "ruby", found: false},
    {language: "Rust", command: "rustc", found: false},
    {language: "Rust", command: "rustup", found: false},
    {language: "Scala", command: "scala", found: false},
    {language: "Swift", command: "swift", found: false},
    {language: "Tcl", command: "tclsh", found: false},
    {language: "Vala", command: "valac", found: false},
    {language: "Zig", command: "zig", found: false},
]

/** @param {string} dir
 * @returns {Promise<string[]>} */
async function listFiles(dir) {
  try {
    const files = await fs.promises.readdir(dir);
    return files;
  } catch (err) {
    console.error(`Error reading directory ${dir}: ${err.message}`);
    process.exit(1);
  }
}

/** @returns {Promise<Set<string>>} */
async function getAllFilesInPath() {
  if (process.env.PATH == null) {
    console.error("PATH environment variable not found");
    process.exit(1);
  }
  const pathDirs = process.env.PATH.split(path.delimiter).filter((dir) => {
    return !(Boolean(dir) === false || dir.includes("/sbin"));
  });
  /** @type string[] */
  const allFiles = [];
  for (const dir of pathDirs) {
    const files = await listFiles(dir);
    allFiles.push(...files);
  }
  return new Set(allFiles);
}

async function main() {
  const files = await getAllFilesInPath();

  for (const entry of LANGUAGES) {
    if (files.has(entry.command)) {
      entry.found = true;
    }
  }

  console.table(LANGUAGES);
}

main();
