# Diseño - todo-list-testing

## Principios aplicados
- SOLID: separación de responsabilidades (Task vs TaskManager vs Repository), inversión de dependencias (TaskManager depende de una interfaz TaskRepository).
- Clean Code: nombres claros, funciones pequeñas, inmutabilidad del modelo Task.
- Testing: TDD (tests cubren creación, validaciones, repositorio en memoria y manager).

## Decisiones
- Repositorio en memoria para simplificar pruebas. En producción se puede implementar una variante que use una base de datos (p. ej. SQLite).
- Task es inmutable (dataclass frozen) para evitar efectos laterales inesperados.