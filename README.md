# Curso-de-F-sica-Computacional
En este repositorio se suben todas las tareas y trabajos realizados durante los cursos de física computacional de la Facultad de Ciencias. El lenguaje de programación es mayormente Python pero en algunos casos podrían subirse cuadernos de Jupyter con el kernel de Julia.

Pasos para utilizar Git y GitHub

1. Crear tu repositorio local. Para ello es necesario introducir `git init`. Esto crea tu repositorio local desde la rama `master`
2. Ver el status de tu repositorio: `git status`, sirve para ver que se va a agregar o que no se va a agregar.
3. Para agregar archivos a tu "commit" se debe realizar: `git add .` si quieres agregar todos los archivos de tu carpeta actual (incluyendo carpetas con sus contenidos). O tienes la opción de agregar archivo por archivo.
4. Realizar commit: `git commit -m "El mensaje que tu quieras"`
5. De aquí nos vamos a crear el repositorio remoto en GitHub, se selecciona `+` y "new repository". Le pones un título, una descripción y te recomiendo NO agregar el archivo `README.md`.
6. Una vez creado se debe de ir a la liga del repositorio y obtenerla para que nuevamente en la terminal se haga `git remote add origin URL`
7. Una vez hecho esto ahora podemos subir nuestros cambios haciendo `git push -u origin master`. Y listo!
8. Si agregaste por error el archivo `README.md` que a mi parecer es importante hacerlo, es probable que al hacer el primer push te haya aparecido un error, este se resuelve con el siguiente comando: `git pull --rebase origin  master`. Lo que sucedió aquí es que el repo de Github tuvo un primer commit que no se registró en el local y ambos deben estar a la par (local y virtual), con este comando lo que haces es poner ambos repositorios a la par, baja el archivo readme a tu repo local y ya con eso puedes proceder con tu push naturalmente.



