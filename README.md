# Programación II - Taller I

Guía práctica para preparar un entorno de desarrollo en Windows con **Visual Studio Code**, **Git**, **GitHub CLI** y **Python**, y publicar este proyecto en GitHub.

## Contenido

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración del proyecto](#configuración-del-proyecto)
- [Publicar el proyecto en GitHub](#publicar-el-proyecto-en-github)
- [Flujo de trabajo diario](#flujo-de-trabajo-diario)
- [Comandos útiles](#comandos-útiles)
- [Solución de problemas](#solución-de-problemas)

## Requisitos

- Windows 10 o posterior.
- Una cuenta de [GitHub](https://github.com/signup).
- Permisos para instalar aplicaciones en el equipo.

## Instalación

Instala las siguientes herramientas desde sus sitios oficiales:

1. [Visual Studio Code](https://code.visualstudio.com/download)
2. [Git](https://git-scm.com/install/)
3. [GitHub CLI](https://cli.github.com/)
4. [Python](https://www.python.org/downloads/)

En Visual Studio Code, instala también la extensión oficial de [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

### Actualizar Git y GitHub CLI

Para actualizar Git para Windows y GitHub CLI, ejecuta:

```powershell
git update-git-for-windows
winget upgrade --id GitHub.cli
```

### Verificar las instalaciones

Abre una terminal de PowerShell y ejecuta:

```powershell
code --version
git --version
gh --version
python --version
```

Si algún comando no se reconoce, reinicia Visual Studio Code o Windows y vuelve a intentarlo.

## Configuración del proyecto

### 1. Crear o abrir la carpeta

Crea la carpeta `ProgramacionIITallerI` dentro de Documentos y abre una terminal en esa ubicación:

```powershell
cd "$HOME\Documents\ProgramacionIITallerI"
```

También puedes abrirla desde Visual Studio Code con **File > Open Folder**.

### 2. Inicializar Git

Si el proyecto todavía no tiene un repositorio local, ejecuta:

```powershell
git init
git branch -M main
```

Comprueba el estado del repositorio:

```powershell
git status
```

## Publicar el proyecto en GitHub

### Opción A: usar GitHub CLI

Autentícate una sola vez:

```powershell
gh auth login
gh auth status
```

Crea el repositorio público y sube el contenido actual:

```powershell
gh repo create ProgramacionIITallerI --public --source=. --remote=origin --push
```

### Opción B: crear el repositorio desde GitHub

1. Crea un repositorio nuevo en [GitHub](https://github.com/new) llamado `ProgramacionIITallerI`.
2. No agregues otro `README.md` si ya existe uno localmente.
3. Conecta el repositorio remoto:

```powershell
git remote add origin https://github.com/TU_USUARIO/ProgramacionIITallerI.git
```

4. Guarda y publica los archivos:

```powershell
git add .
git commit -m "Inicializa el proyecto"
git push -u origin main
```

Reemplaza `TU_USUARIO` por tu nombre de usuario de GitHub.

## Flujo de trabajo diario

Antes de comenzar, actualiza tu copia local:

```powershell
git pull origin main
```

Después de realizar cambios:

```powershell
git status
git add .
git commit -m "Describe brevemente el cambio"
git push origin main
```

Los mensajes de commit deben ser breves y explicar qué cambió. Por ejemplo:

```text
Agrega ejercicios de listas
Corrige la validación de entradas
Actualiza la documentación
```

## Comandos útiles

| Comando | Descripción |
| --- | --- |
| `git status` | Muestra los archivos modificados. |
| `git log --oneline` | Muestra el historial resumido. |
| `git diff` | Muestra cambios que aún no se han preparado. |
| `git remote -v` | Muestra los repositorios remotos configurados. |
| `gh repo view --web` | Abre el repositorio actual en el navegador. |
| `python archivo.py` | Ejecuta un archivo de Python. |

## Solución de problemas

### `git` o `gh` no se reconoce

Verifica que la herramienta esté instalada y reinicia la terminal para actualizar el `PATH`.

### GitHub solicita autenticación

Ejecuta `gh auth login` y sigue las instrucciones del navegador. Después confirma el estado con `gh auth status`.

### El repositorio remoto ya existe

Consulta el remoto configurado antes de agregarlo nuevamente:

```powershell
git remote -v
```

Si la URL es incorrecta, actualízala con:

```powershell
git remote set-url origin https://github.com/TU_USUARIO/ProgramacionIITallerI.git
```

## Buenas prácticas

- Mantén el `README.md` actualizado cuando cambie la forma de ejecutar el proyecto.
- Usa nombres descriptivos para archivos, ramas y commits.
- No subas contraseñas, tokens ni claves privadas al repositorio.
- Revisa `git status` antes de cada commit.
- Trabaja en ramas separadas cuando desarrolles funcionalidades nuevas.
