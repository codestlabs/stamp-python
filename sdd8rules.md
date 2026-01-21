# SDD8 Rules – Software Development Design
1. - Max line length: 126 characters. Only exceed if readability improves.  
2. - Minimize newlines; separate logical sections only.  
3. - Indentation: tabs only, no spaces.  
4. - Module structure: imports → constants → classes → functions → main execution.  
5. - Class/Function size: ≤ 400 lines; split large modules logically.  
6. - Functions / methods: camelCase (myFunction).  
7. - Files / modules: snake_case (my_module.py).  
8. - Classes: UpperCamelCase (MyClass).  
9. - Constants: all caps with underscores (MY_CONSTANT).  
10. - Variables: descriptive; single letters only in loops (i, j).  
11. - Functions ≤ 40 lines; break longer functions into helpers.  
12. - Classes: one responsibility per class.  
13. - Method order: __init__ → public methods → private helpers → static methods.  
14. - Prefer composition over inheritance unless necessary.  
15. - Double quotes consistently ("text").  
16. - No trailing spaces; minimal extra spaces inside brackets/parentheses.  
17. - Multi-line strings: use implicit concatenation, not backslashes.  
18. - Comment sparingly; only for non-obvious logic.  
19. - Inline comments: concise (x += 1  # increment counter).  
20. - Docstrings optional; short, descriptive for public APIs only.  
21. - Import order: local (relative, if package) → third-party → standard.  
22. - No wildcard imports (from module import *).  
23. - Avoid circular dependencies.  
24. - Keep try/except blocks focused; avoid wrapping entire functions.  
25. - Custom exceptions for module-specific errors; avoid generic ones.  
26. - Clarity over compactness; avoid nested ternaries.  
27. - Minimize globals; pass parameters explicitly.  
28. - Return statements direct; avoid unnecessary intermediates.  
29. - Keep testable units small; one function → one purpose.  
30. - Write unit tests for critical logic, aim for 80%+ coverage.  
31. - Prefer descriptive test names over numbers (testLoginFailsWithoutPassword).  
32. - Avoid magic numbers; use constants instead.  
33. - Separate configuration from code; use YAML/JSON/ENV files.  
34. - Keep functions pure when possible; avoid side-effects.  
35. - Limit nested loops to 2 levels; refactor deeper logic.  
36. - Keep method parameters ≤ 5; use dataclasses for complex data.  
37. - Avoid hardcoding paths; use os.path.join or pathlib.  
38. - Favor exceptions over return codes for error handling.  
39. - Avoid print statements; use logging utilities for output.  
40. - Limit module dependencies; keep the dependency graph shallow.  
41. - Prefer list/dict comprehensions for simple transformations.  
42. - Avoid deeply nested if/else; consider early returns.  
43. - Use consistent naming for related modules/classes.  
44. - Prefer `with` statements for resource management (files, locks).  
45. - Document all public interfaces, minimal for private helpers.  
46. - Avoid shadowing built-in names (list, dict, str, etc.).  
47. - Keep boolean flags clear; avoid double negatives.  
48. - Use type hints consistently; include return types.  
49. - Avoid over-commenting trivial code; focus on intention.  
50. - Separate UI, logic, and data handling in modules.  
51. - Prefer standard library over external libraries if possible.  
52. - Avoid unnecessary lambdas; prefer named functions.  
53. - Avoid deep inheritance hierarchies; composition first.  
54. - Reuse helper functions across modules; DRY principle.  
55. - Keep exception messages descriptive; include context.  
56. - Avoid mixing concerns in one module (UI + DB + logic).  
57. - Use meaningful logging levels: debug/info/warn/error/critical consistently.  
58. - Use escaping (e.g. "\n\t\r") mostly.
