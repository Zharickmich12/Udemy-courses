# ¿Qué es NestJS y por qué usarlo?

- Framework backend progresivo basado en Node.js y TypeScript. Usa arquitectura modular e inyección de dependencias.
- Usa una arquitectura modular y orientada a clases.
- **Su objetivo:** crear aplicaciones escalables, mantenibles y bien estructuradas.
- **Por qué usarlo →** escalabilidad, mantenibilidad y estructura limpia.

## ¿Por qué usar NestJS?

- Usa TypeScript de forma nativa.
- Estructura clara (módulos, controladores, servicios).
- Facilita la inyección de dependencias.
- Compatible con ORMs (TypeORM, Prisma, Sequelize).
- Soporta testing, middlewares, guards, interceptors y más.

## Conceptos

- **CLI:** genera módulos, controladores y servicios (nest generate module|controller|service).
- **Controladores:** manejan rutas (decoradores @Controller, @Get, @Post...).
- **Servicios:** contienen la lógica de negocio, se inyectan con @Injectable().
- **Inyección de dependencias:** Nest crea e inyecta instancias automáticamente a través de Providers.

## Arquitectura base

- **AppModule:** módulo raíz.
- **Controllers:** manejan las rutas y peticiones HTTP.
- **Services (Providers):** contienen la lógica de negocio.
- **Modules:** agrupan y organizan el código por áreas funcionales.

**Flujo general:** Request → Controller → Service → Repository/DB → Response

## Decoradores esenciales

**Decoradores =** metadatos que Nest usa para saber qué hace cada clase o método.

| Decorador                         | Se usa en  | Función                                  |
| --------------------------------- | ---------- | ---------------------------------------- |
| `@Module()`                       | módulos    | Agrupa controladores, servicios, imports |
| `@Controller()`                   | clases     | Define un controlador (ruta base)        |
| `@Injectable()`                   | clases     | Marca un servicio que puede inyectarse   |
| `@Get()`, `@Post()`               | métodos    | Define rutas HTTP                        |
| `@Body()`, `@Param()`, `@Query()` | parámetros | Extrae datos de la petición              |

## CLI de NestJS

- Herramienta para generar y gestionar tu proyecto rápido.
- Comandos útiles:

  **Instalar Nest.js CLI: (Command line interface)** npm i -g @nestjs/cli

  **Nuevo proyecto: en el path actual** nest new nombre-proyecto

  nest generate module users

  nest generate controller users

  nest generate service users

  **Mostrar ayuda: en cualquier comando:**

  nest -h

  nest g -h

  nest g s nombre -h

## Ciclo de vida de la app

- NestJS inicializa módulos, inyecta dependencias y levanta el servidor con main.ts.

  async function bootstrap() {

  const app = await NestFactory.create(AppModule);

  await app.listen(3000);

  }

  bootstrap();

## Inyección de dependencias (DI)

- Permite que las clases reciban objetos o servicios sin crearlos directamente.
- Nest se encarga de crear e inyectar las instancias.

  @Injectable()

  export class UsersService {

  findAll() { return ['User1', 'User2']; }

  }

  @Controller('users')

  export class UsersController {

  constructor(private readonly usersService: UsersService) {}

  }

## Providers

- Todo lo que puede inyectarse en otro lugar (servicios, repositorios, factories).
- Se declaran en la propiedad providers dentro del módulo.

## Pipes, Guards, Interceptors (visión general)

- **Pipes:** validan o transforman datos de entrada.
- **Guards:** controlan el acceso a rutas.
- **Interceptors:** modifican la respuesta o el flujo de ejecución.

## Buenas prácticas iniciales

- Separar la lógica de negocio (servicios) de la lógica HTTP (controladores).
- Un módulo por funcionalidad.
- Nombrar carpetas y archivos con consistencia.
- Usar DTOs para validar datos desde el inicio.
