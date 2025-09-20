# TLP Interpreter

A custom programming language interpreter built in Python, following the principles from "Writing an Interpreter in Go" but implemented in Python. TLP (The Legend Paras Language) is a dynamically typed programming language with C-like syntax that supports variables, functions, expressions, and control flow.
## 📚 Learning Resources

This project is based on the excellent book ["Writing an Interpreter in Go"](https://interpreterbook.com/) by Thorsten Ball, but implemented in Python to demonstrate language implementation concepts.

### Key Learning Concepts
- **Lexical Analysis**: How to break source code into meaningful tokens
- **Recursive Descent Parsing**: Building parsers for programming languages  
- **Pratt Parsing**: Elegant handling of operator precedence
- **AST Design**: Representing program structure in memory
- **Interpreter Architecture**: Component organization and interaction
## 🚀 Features

### Current Implementation
- **Lexical Analysis**: Complete tokenizer that breaks source code into tokens
- **Parsing**: Pratt parser implementation supporting infix and prefix expressions
- **AST Generation**: Abstract Syntax Tree construction for program representation
- **REPL**: Interactive Read-Eval-Print Loop for testing and experimentation
- **Expression Evaluation**: Support for mathematical and logical expressions

### Supported Language Constructs
- **Variables**: `let` statements for variable declarations
- **Functions**: Function definitions with `fn` keyword
- **Control Flow**: `if`/`else` statements and `return` statements
- **Data Types**: Integers, booleans (`true`/`false`)
- **Operators**: 
  - Arithmetic: `+`, `-`, `*`, `/`
  - Comparison: `==`, `!=`, `<`, `>`
  - Logical: `!` (bang/not operator)
- **Expressions**: Both prefix (`-x`, `!x`) and infix (`x + y`) expressions




### Running the REPL
```bash
python TPL_main.py
```

### Example Usage
```javascript
>> let x = 5;
>> let y = 10;
>> let result = x + y * 2;
>> result
25
```

## 🧪 Testing

The project includes comprehensive unit tests:

```bash
# Run lexer tests
python lexer_test.py

# Run parser tests
python parser_test.py

# Run AST tests
python ast_test.py
```

### Test Coverage
- **Lexer Tests**: Token generation and recognition
- **Parser Tests**: AST construction and precedence handling
- **Integration Tests**: End-to-end parsing scenarios

## 🔮 Future Enhancements

### Planned Features (from TODO)
1. **Machine Learning Integration**: AI-powered code completion and optimization
2. **Unicode Support**: Full Unicode and emoji support in identifiers and strings



## 📄 License

This project contains reference materials from "Writing an Interpreter in Go" which are licensed under MIT license. The TLP interpreter implementation follows the same licensing terms.

## 👨‍💻 Author

**Paras** (thelegendparas)
- GitHub: [@thelegendparas](https://github.com/thelegendparas)
- 4th Year Computer Science Engineering Student

---
