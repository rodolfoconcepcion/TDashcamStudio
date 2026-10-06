with open('/home/rodolfo/TDashcamStudio/src/script.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
in_en = False
in_es = False
for line in lines:
    if line.strip() == 'en: {':
        in_en = True
    elif line.strip() == 'es: {':
        in_es = True
    
    if in_en and line.strip() == '},':
        new_lines.extend([
            '        clearDate: "Clear Date",\n',
            '        toggleMetadata: "Toggle Metadata (Dashboard)",\n',
            '        legacy: "PIP View",\n',
            '        grid4: "4-Grid View",\n',
            '        grid6: "6-Grid View",\n',
            '        detailedMetadata: "Detailed Metadata",\n',
            '        exportMetadataCSV: "Export Metadata to CSV",\n',
            '        mergeGridVideo: "Merge 4-Grid Video",\n',
            '        toggleThemeTip: "Toggle Light/Dark Theme",\n',
            '        revealFileTip: "Reveal File Path",\n',
            '        copyPath: "Copy Path",\n',
            '        openSidebar: "Open Sidebar",\n',
            '        useFFmpeg: "Export with FFmpeg (Fast)",\n',
            '        useFFmpegTip: "Use local FFmpeg binary if available for blazing fast export",\n',
            '        addMetadataHUD: "Add Metadata Overlay",\n',
            '        downloadVideoTip: "Download Video",\n'
        ])
        in_en = False
    elif in_es and line.strip() == '},':
        new_lines.extend([
            '        clearDate: "Limpiar Fecha",\n',
            '        toggleMetadata: "Alternar Metadatos (Panel)",\n',
            '        legacy: "Vista PIP",\n',
            '        grid4: "Vista 4 Cámaras",\n',
            '        grid6: "Vista 6 Cámaras",\n',
            '        detailedMetadata: "Metadatos Detallados",\n',
            '        exportMetadataCSV: "Exportar Metadatos a CSV",\n',
            '        mergeGridVideo: "Combinar Pista de Video",\n',
            '        toggleThemeTip: "Cambiar Tema Claro/Oscuro",\n',
            '        revealFileTip: "Mostrar Ruta de Archivo",\n',
            '        copyPath: "Copiar Ruta",\n',
            '        openSidebar: "Abrir Panel Lateral",\n',
            '        useFFmpeg: "Exportar con FFmpeg (Rápido)",\n',
            '        useFFmpegTip: "Usar binario local de FFmpeg para exportación rápida",\n',
            '        addMetadataHUD: "Añadir Superposición",\n',
            '        downloadVideoTip: "Descargar Video",\n',
            '        clipStartTime: "Hora de Inicio:",\n',
            '        clipEndTime: "Hora de Fin:",\n',
            '        gear: "Marcha",\n',
            '        gps: "GPS",\n',
            '        speed: "Velocidad",\n',
            '        moreOptions: "Más Opciones",\n',
            '        exportClip: "Exportar Corte",\n',
            '        accelerator: "Acelerador",\n',
            '        clipDuration: "Duración:",\n',
            '        addTimestamp: "Añadir Marca de Tiempo",\n',
            '        brake: "Freno",\n',
            '        blinker: "Direccional",\n',
            '        confirmClip: "Confirmar Corte",\n',
            '        steering: "Volante",\n'
        ])
        in_es = False
        
    new_lines.append(line)

with open('/home/rodolfo/TDashcamStudio/src/script.js', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
