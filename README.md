![Logo](https://data1.ibtimes.co.in/en/full/433631/minecraft.jpg)

# Introduccion

Este documento sera la biblia para poder hostear mi servidor de Minecraft. Sera una guia de instalacion y configuracion y automatizacion de todo lo que necesite.

## Metadata

Version de Minecraft: 1.20.1

Modloader: Forge 47.3.0

Mods: ~100

# Tutorial

## Instalación

A continuación se detalla el paso a paso para instalar un cliente que pueda conectarse al servidor

1. Instalar un launcher de Minecraft. Puede ser el oficial desde la [página de Minecraft](https://www.minecraft.net/es-es/download) o alguno pirata de su preferencia. Las instrucciones sennaladas en este tutorial solo son validas para el launcher oficial.
2. Abrir el launcher.
3. Crear una nueva instalación vanilla, para esto:
   1. En la parte superior del cliente ir a Instalaciones/Installations
   2. Seleccionar "Nueva Instalación"/"New Installation"
   3. De nombre escribir 1.20.1 Vanilla o algo similar
   4. En "Version" seleccionar "`release 1.20.1`" (no la "`snapshot 1.20.1-rc1`")
   5. Crear la instalación (botón Crear/Create en la esquina inferior derecha)
   6. Ejecutar la instalación creada (botón Jugar/Play)
4. Cuando se vea el menú principal del juego, cerrarlo.
5. Instalar Iris
   1. Descargar y ejecutar el instalador desde la [página oficial](https://www.irisshaders.dev/download) (JAR Universal)
   2. Seleccionar la versión correcta (1.20.1)
   3. Seleccionar "Iris Only" en vez de "Iris + Fabric"
   4. Presionar el botón Install
6. Instalar Forge
   1. Descargar y ejecutar el instalador desde la [página oficial](https://files.minecraftforge.net/net/minecraftforge/forge/). Debe ser la versión 47.3.0. También se puede usar el [link directo](https://maven.minecraftforge.net/net/minecraftforge/forge/1.20.1-47.3.0/forge-1.20.1-47.3.0-installer.jar)
   2. Presionar "Ok"
7. Descargar los mods
   1. Ir a la parte superior de esta página y apretar el botón verde "Code"
   2. Apretar "Descargar ZIP"
   3. Descomprimir el zip descargado
   4. Copiar los mods en la carpeta `.minecraft/mods` (crearla si es que no está). Para acceder a esta carpeta hay que apretar WIN + R (mantener la tecla de Windows y apretar la R), y escribir `%appdata%` y apretar enter.

Para iniciar el cliente hay que revisar que esté seleccionada la versión Forge 1.20.1 (no la instalación Vanilla que crearon)

Después de descargar y meter los mods, se pueden eliminar los siguientes mods que no son necesarios por parte de los clientes:

- [AppleSkin](https://www.curseforge.com/minecraft/mc-mods/appleskin): Mejora visual para el HUD respecto a la comida
- [JEI](https://www.curseforge.com/minecraft/mc-mods/jei): Muestra todos los items y sus recetas y usos
- [JER](https://www.curseforge.com/minecraft/mc-mods/just-enough-resources-jer): JEI Addon para recursos
- [JADE](https://www.curseforge.com/minecraft/mc-mods/jade): HWYLA
- [Enchantment Descriptions](https://www.curseforge.com/minecraft/mc-mods/enchantment-descriptions): Muestra las descripciones de los encantamientos
- [Xaero's Minimap](https://www.curseforge.com/minecraft/mc-mods/xaeros-minimap): Minimapa
- [Xaero's Worldmap](https://www.curseforge.com/minecraft/mc-mods/xaeros-world-map): Mapa del mundo
- [Ambient Sounds](https://www.curseforge.com/minecraft/mc-mods/ambientsounds): Sonidos ambientales
- [Inventory HUD+](https://www.curseforge.com/minecraft/mc-mods/inventory-hud-forge): Interfaz para tener el inventario siempre visible
- [AI Improvements](https://www.curseforge.com/minecraft/mc-mods/ai-improvements): Mejoras de rendimiento relacionadas con la IA
- [Not Enough Animations](https://www.curseforge.com/minecraft/mc-mods/not-enough-animations): Animaciones en tercera persona
- [First Person Model](https://www.curseforge.com/minecraft/mc-mods/first-person-model): Primera persona mas inmersiva
- [Skin Layers 3D](https://www.curseforge.com/minecraft/mc-mods/skin-layers-3d): Le da profundidad a los modelos de personaje
- [Sound Physics](https://www.curseforge.com/minecraft/mc-mods/sound-physics-remastered): Sonidos con fisicas reales
- [Falling Leaves](https://www.curseforge.com/minecraft/mc-mods/falling-leaves-forge): Hojas que caen de los arboles
- [What Are They Up To](https://www.curseforge.com/minecraft/mc-mods/what-are-they-up-to): Permite ver que hacen los demas jugadores
- [Falling Tree](https://www.curseforge.com/minecraft/mc-mods/falling-tree): Talar arboles enteros de un golpe
- [Pick Up Norifier](https://www.curseforge.com/minecraft/mc-mods/pick-up-notifier): Notificaciones de los bloques recogidos

## Conexión

La IP del servidor es

`minecraft.tokosan.cl`

## Changelog

### 2024-08-06

1. Eliminar Better Combat
2. Añadir lo siguiente:
   1. [Epic Fight Mod](https://mediafilez.forgecdn.net/files/5601/221/epicfight-forge-20.8.5-1.20.1.jar)
   2. [EFM Compat](https://mediafilez.forgecdn.net/files/5214/748/EFMCompat%202.0.jar)
   3. [Weapons of Miracles](https://mediafilez.forgecdn.net/files/5598/482/WeaponsOfMiracles-20.1.8.5.1.jar)
   4. [Battle Arts](https://mediafilez.forgecdn.net/files/5596/596/EpicFightBA-20.8.5.6.jar)
   5. [JRFTL](https://mediafilez.forgecdn.net/files/4594/475/JRFTL-1.20.1-1.6.0.jar)
   6. [EFMEX](https://mediafilez.forgecdn.net/files/5594/746/EpicFightExCap-20.8.1.jar)
