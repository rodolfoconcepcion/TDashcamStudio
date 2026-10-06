<p align="center">
  <img src="src/logo-small.png" alt="TeslaCam Studio Logo" width="80" height="80">
</p>
<h1 align="center">TeslaCam Studio</h1>

<p align="center"><a href="README.md">English</a> | Español | <a href="README_ZH.md">简体中文</a></p>

<p align="center">
  <a href="https://github.com/rodolfoconcepcion/TeslaCamStudio/releases"><img src="https://img.shields.io/github/v/release/rodolfoconcepcion/TeslaCamStudio?style=flat-square&color=blue" alt="Release"></a>
  <a href="https://github.com/rodolfoconcepcion/TeslaCamStudio/releases"><img src="https://img.shields.io/github/downloads/rodolfoconcepcion/TeslaCamStudio/total?style=flat-square&color=green" alt="Downloads"></a>
  <a href="https://github.com/rodolfoconcepcion/TeslaCamStudio/blob/main/LICENSE"><img src="https://img.shields.io/github/license/rodolfoconcepcion/TeslaCamStudio?style=flat-square" alt="License"></a>
  <a href="https://github.com/rodolfoconcepcion/TeslaCamStudio/stargazers"><img src="https://img.shields.io/github/stars/rodolfoconcepcion/TeslaCamStudio?style=flat-square" alt="Stars"></a>
  <a href="https://github.com/rodolfoconcepcion/TeslaCamStudio/actions/workflows/build.yml"><img src="https://img.shields.io/github/actions/workflow/status/rodolfoconcepcion/TeslaCamStudio/build.yml?style=flat-square&label=CI" alt="CI"></a>
</p>

Un moderno reproductor para los videos de tu cámara Tesla (Dashcam). Reproduce de forma simultánea y sincronizada los seis ángulos de cámara (Frontal, Trasero, Izquierdo, Derecho, Pilares B) con una interfaz intuitiva. ¡Ahora disponible como **aplicación de escritorio**!

## 🆚 ¿Por qué elegir TeslaCam Studio?

A diferencia del reproductor nativo en el vehículo o reproductores de video simples, este proyecto ofrece características superiores y una experiencia más potente:

| Característica | Reproductor en el Vehículo | Reproductor Nativo en PC | TeslaCam Studio (Este Proyecto) |
| :--- | :--- | :--- | :--- |
| **Reproducción Sincronizada** | ✅ 6 cámaras soportadas | ❌ Apertura manual, no sincroniza | ✅ **Sincronización perfecta de 6 canales, diseño intuitivo** |
| **Visualización** | Limitada a la pantalla del auto | Pantalla grande, carpetas desorganizadas | **Multi-dispositivo**, pantalla grande, eventos organizados |
| **Filtrado** | Categorías básicas | ❌ Búsqueda manual en carpetas | ✅ **Filtro inteligente por fecha, hora y evento** |
| **Datos de Cond.** | ✅ Soporta metadatos | ❌ Sin acceso a datos ocultos (solo video) | ✅ **Panel de Datos: Velocidad, Pedales, FSD, Ángulo, etc.** |
| **Edición/Corte** | ❌ No soportado | ❌ Requiere herramientas (Premiere/FFmpeg) | ✅ **Corte visual, arrastrar y soltar con marca de agua** |
| **Exportación** | ❌ Difícil de exportar | ❌ Solo fragmentos originales | ✅ **Exportación en Cuadrícula (Mosaico) a un clic** |
| **Mapa/GPS** | Mapa básico en consola | ❌ No utiliza datos de GPS | ✅ **Nombres de calle + Enlaces ocultos a Google Maps** |
| **Privacidad** | - | ✅ Procesamiento Local | ✅ **Procesamiento 100% Local**, enfocado en privacidad |

![Screenshot](./.github/assets/home.webp)

## 📺 Demostración de Características

| Característica | Demostración |
| :--- | :--- |
| **Inicio Rápido**: Solo tienes que arrastrar y soltar la carpeta para empezar a usarlo | ![Quick Start](.github/assets/GIF/drop-open.webp) |
| **Diseño Moderno**: Modo Claro/Oscuro dinámico con soporte del sistema y animaciones | ![Modern UI](.github/assets/GIF/ui.gif) |
| **Búsqueda Avanzada**: Encuentra grabaciones por fecha y clasificaciones de la propia memoria | ![Smart Filtering](.github/assets/GIF/filter.gif) |
| **Integración de Mapas**: Nombres de las calles e integraciones directas para abrir mapas | ![Map Integration](.github/assets/GIF/map.webp) |
| **Velocidad Ajustable**: Controla el ritmo del video entre 0.5x y 2.0x | ![Playback Speed](.github/assets/GIF/speed.gif) |
| **Telemetría Vehicular**: Observa la velocidad, pedales (acelerador/freno), direccionales y Autopilot. | ![Driving Data](.github/assets/GIF/meta-data.webp) |
| **Curva de Velocidad**: Identifica aceleraciones o frenadas repentinas a través del gráfico visible en la duración del clip | ![Speed Curve](.github/assets/GIF/speed-curve.webp) |
| **Exportar Datos**: Exporta de a un clic tus metadatos (CSV) para auditoría de conducción | ![Data Export](.github/assets/GIF/csv-export.webp) |
| **Reproducción Simultanea**: Organízalo de múltiples esquemas de visualizaciones para 6 cámaras | ![Sync Playback](.github/assets/GIF/play.webp) |
| **Exportación Visual**: Exporta videos sin usar FFmpeg por tu lado, todo visual de forma precisa. | ![Visual Clipping](.github/assets/GIF/export.webp) |
| **Resultados (Mosaicos)**: Videos integrados listos con los Metadatos montados como marca de agua | ![Export Results](.github/assets/GIF/6-exported-play.webp) |

## ✨ Características Detalladas

### 🎥 Reproductor y Visualización
*   **Diseños Especiales**: Hasta cuatro configuraciones de pantallas para visualizar desde pantalla completa hasta malla 6x6.
*   **Cámaras B-Pillar**: Cobertura amplia para los puntos siegos ubicados en las columnas B del interior.
*   **Telemetría y Metadatos de SEI**: Muestra todos los sistemas integrados de Tesla usando los metadatos de los mp4 (Direccionales, FSD, Frenos, Velocidad y Posición del Guía).
*   **Curvas y Gráficos Visuales**: Los tiempos clave se reflejan de fondo junto a la reproducción.
*   **Rastreabilidad en Mapas**: Utiliza las coordenadas del Dashcam para mostrar las señales en Mapas de forma instantanea (Google Maps) con un simple clic.

> **Nota:** La información vehicular es exclusiva de los vehículos integrados con metadatos utilizando las actualizaciones mayores al Sistema **2025.44.25.11**.

![Metadata Display 1](.github/assets/screenshot1.webp)
![Metadata Display 2](.github/assets/screenshot2.webp)

### ✂️ Edición y Mosaicos Múltiples

*   **Segmentación Directa (Cortes)**: Desplázate con controles para generar cortes perfectos solo usando arrastrar y soltar (Drag and Drop).
*   **Concatenación de minutos Múltiples**: Si vas a cortar más de 1 minuto continuo, los enlaces están hechos sin cortes visuales en los fragmentos generados por el Dashcam de Tesla en crudo de forma automática.
*   **Montajes Listos**: Exporta una cuadretera 2x3 de cámara e incluye el estampado en tiempo real del reporte de telemetría (Tiempo, Marca, Ángulos, Frenos, Velocidad) sobrepuesto en la grabación de prueba.
*   **Selectores de Exportación Visuales**: Puedes apagar cualquier cámara que no quieras generar dentro de la exportación (Ejemplo dejar solo las 3 frontales).

### 🎨 Arquitectura de Estilo Moderno
*   **Temas Duales**: Transición sin pausas del Modo Claro hacia el Modo Oscuro según los ajustes del OS.
*   **Multilenguaje Nivel Experto**: Integración Completa para Inglés (Predefinido), Español y Chino (Legacy) basado en las reglas del navegador.
*   **Optimización 100% Localizada**: Privacidad extrema lograda mediante Canvas API & MediaRecorder. Todos los procesamientos son locales de tú PC o servidor Homelab de inicio a fin. No procesamientos externos para edición de video.

## 🚀 Como instalar o Ejecutar

### 🖥️ Aplicación de Escritorio (Opcional)

Descarga la aplicación respectiva a través de los lanzamientos usando la pagina oficial de Descargas [Releases](https://github.com/rodolfoconcepcion/TeslaCamStudio/releases):

| Plataforma | Descarga |
|----------|----------|
| Windows | `.exe` / `.msi` |
| macOS (Apple Silicon) | `.dmg` (aarch64) |
| macOS (Intel) | `.dmg` (x64) |
| Linux | `.deb` / `.AppImage` |

> **Nota para MacOS:**
> Debido al sistema rigido de cuarentena, si Apple te arroja un aviso de "Archivo dañado" ejecuta la corrección pertinente en tu consola:
> ```bash
> sudo xattr -rd com.apple.quarantine /Applications/TeslaCam\ Studio.app
> ```

---

### 💻 Despliegue en Homelab de Forma Local vía Servidor Web.

Debido a las politicas seguras del CORS originada por el acceso web directo a un folder/USB en crudo es estrictamente recomendado arrancar o correr desde un Servidor por razones de Seguridad.

**1. Mediante Contenedores Docker (Opción Definitiva y Recomendada)**

Puedes correr instantáneamente con el archivo docker en Runtipi o un servidor remoto docker host en general:

1.  **Ejecutar Instalación del App:**
    ```bash
    docker compose up -d
    ```

2.  **Abriendo Localmente:**
    Abre tu URL designada o utilizando el Localhost: `http://localhost:8188`.

3.  **Para apagar la Plataforma:**
    ```bash
    docker compose down
    ```

**2. A través de Servidores Node.js**
Si cuentas con librerías nativas usando Node.js, `npx` funciona excelente.
```bash
npx http-server -p 8188 src
```

## 🔒 Estándares y Politicas de Privacidad.
La esencia del sistema fue estructurada pensando en no compartir los videos ni localización que contiene la Tesla Flashdrive. Tu computadora descarga las librerías necesarias y tu CPU se encarga nativamente de los cortes. La Nube y Servidores externos **no tocan** el material sensible. Tus carpetas, la interfaz gráfica y tu explorador de disco son la misma herramienta unificada para tú beneficio.

## 📄 Licencia
Licencia Estándar AGPL-3.0
