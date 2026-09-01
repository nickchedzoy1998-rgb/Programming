# Advanced Programming — University of Helsinki

My solutions for Parts 8–12 of the University of Helsinki Advanced Course in Programming with Python. This curated collection contains 77 exercises covering object-oriented programming, functional techniques, recursion, file and JSON processing, regular expressions, generators, and larger command-line applications.

Each exercise directory contains the original brief in `exercise.md` and my Python solution. The full course remains an ongoing learning goal; this collection documents the material currently completed and prepared for public review.

## Highlights

### [Order Book Application](<Part_11/19_order_book_application/order_book_application.py>)

This command-line task manager separates domain objects from interaction logic. `Task` owns identity and completion state, `OrderBook` manages querying and workload statistics, and `OrderBookApplication` handles commands and input validation. It showcases object-oriented decomposition, class-level state, collection operations, exceptions, reporting, and assembling smaller abstractions into a complete application.

### [Hockey Statistics Explorer](<Part_12/15_hockey_statistics/hockey_statistics.py>)

This application loads structured player data from JSON and supports searches, grouping, rankings, and formatted reports. Its sorting rules combine points, goals, and games to resolve rankings correctly. It showcases path-safe file I/O, JSON processing, filtering, set-based uniqueness, compound sort keys, presentation formatting, and separation of data logic from the command-line interface.

### [Word Game Framework](<Part_10/04_word_game/word_game.py>)

A reusable base game class defines the shared round and scoring workflow, while subclasses implement longest-word, most-vowels, and rock-paper-scissors rules by overriding a single method. It showcases inheritance, polymorphism, method overriding, shared control flow, and designing code that can be extended without duplicating the surrounding application logic.

### [Item, Suitcase, and Cargo Hold](<Part_09/15_item_suitcase_hold/code_1.py>)

A nested object model enforces weight constraints as items are placed into suitcases and suitcases into a cargo hold. It demonstrates composition, encapsulation, aggregation across object collections, domain invariants, and readable object representations.

## Course Progress

| Part | Exercises | Topics |
|---|---:|---|
| [Part 8](Part_08/) | 16 | Classes, objects, constructors, methods, and object collections |
| [Part 9](Part_09/) | 15 | Encapsulation, class relationships, objects as values, and larger models |
| [Part 10](Part_10/) | 12 | Inheritance, application architecture, custom operators, and class hierarchies |
| [Part 11](Part_11/) | 19 | Comprehensions, recursion, generators, functional techniques, and trees |
| [Part 12](Part_12/) | 15 | Files, CSV/JSON data, regular expressions, randomness, and data analysis |
| **Total** | **77** | Curated solutions currently included |

## Capabilities Demonstrated

- Designing cohesive classes with clear responsibilities and controlled state
- Modelling real-world relationships through composition and inheritance
- Building command-line applications around reusable domain logic
- Processing collections with comprehensions, generators, filters, and custom sorting
- Traversing recursive structures and applying recursive problem-solving techniques
- Reading, validating, transforming, and reporting on external data
- Using type hints, special methods, exceptions, regular expressions, and filesystem-safe paths

## Navigation

Exercises are numbered in course order inside each part. Open a folder to review its `exercise.md` brief and corresponding `.py` solution together. The [repository README](../README.md) provides a cross-collection portfolio overview.
