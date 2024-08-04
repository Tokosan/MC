![Logo](https://data1.ibtimes.co.in/en/full/433631/minecraft.jpg)

# Introduccion

Este documento sera la biblia para poder hostear mi servidor de Minecraft. Sera una guia de instalacion y configuracion y automatizacion de todo lo que necesite.

## Metadata

Version de Minecraft: 1.20.1

Modloader: Forge 47.3.0

Mods: ~100

## Objetivos

El objetivo de hostear los archivos en anakena es tener una especie de "backup" o repositorio desde el cual poder obtener todos los mods necesarios en caso de querer volver a abrir el servidor en otra maquina.

Como objetivos tengo:

1. Tener instrucciones de como iniciar el servidor desde cero, y como descargar los mods desde aca
2. Tener un listado de los mods utilizados y sus descripciones

## Tutoriales

Para iniciar tuve que ver algunos tutoriales, de los que destaco y no quiero perder:

1. [Como usar Iris con Forge](https://www.youtube.com/watch?v=NPNzp4N05xg)
2. [Versiones de Oculus + Rubidium](https://www.youtube.com/watch?v=dOckgD2W8_0)
3. [Versiones de Create + Rubidium](https://www.reddit.com/r/CreateMod/comments/16r1cow/can_not_start_game_with_create_and_rubidium/)

# Instalacion

## Cliente

A continuación se detalla el paso a paso para instalar un cliente que pueda conectarse al servidor

1. Instalar el launcher de Minecraft desde la [página oficial](https://www.minecraft.net/es-es/download)
2. Crear una nueva instalación vanilla, para esto:
   1. En la parte superior del cliente ir a Instalaciones/Installations
   2. Seleccionar "Nueva Instalación"/"New Installation"
   3. De nombre escribir 1.20.1 Vanilla o algo similar
   4. En "Version" seleccionar "`release 1.20.1`" (no la "`snapshot 1.20.1-rc1`")
   5. Crear la instalación (botón Crear/Create en la esquina inferior derecha)
   6. Ejecutar la instalación creada (botón Jugar/Play)
3. Cuando se vea el menú principal del juego, cerrarlo.
4. Instalar Iris
   1. Descargar y ejecutar el instalador desde la [página oficial](https://www.irisshaders.dev/download)
   2. Seleccionar la versión correcta (1.20.1)
   3. Seleccionar "Iris Only" en vez de "Iris + Fabric"
   4. Presionar el botón Install
5. Instalar Forge
   1. Descargar y ejecutar el instalador desde la [página oficial](https://files.minecraftforge.net/net/minecraftforge/forge/). Debe ser la versión 47.3.0. También se puede usar el [link directo](https://maven.minecraftforge.net/net/minecraftforge/forge/1.20.1-47.3.0/forge-1.20.1-47.3.0-installer.jar)
   2. Presionar "Ok"
6. Instalar los mods
   1. Usar el script de Python aaaaa que lindo que será!!!

# Mods

## Para conversar

Los mods polemicos que hay que analizar son:

1. [Farmer's Delight](https://www.curseforge.com/minecraft/mc-mods/farmers-delight)
2. [Supplementaries](https://www.curseforge.com/minecraft/mc-mods/supplementaries)
3. [Rotten Flesh to Leather](https://www.curseforge.com/minecraft/mc-mods/rotten-flesh-to-leather-1-20-1)
4. [Ars Nooveau](https://www.curseforge.com/minecraft/mc-mods/ars-nouveau)
5. [Security Craft](https://www.curseforge.com/minecraft/mc-mods/security-craft)

### Combat

1. [Better Combat](https://www.curseforge.com/minecraft/mc-mods/better-combat-by-daedelus)
2. Addons de Better Combat: [Paladins & Priests](https://www.curseforge.com/minecraft/mc-mods/paladins-and-priests), [Wizards](https://www.curseforge.com/minecraft/mc-mods/wizards), etc.
3. [Simply Swords](https://www.curseforge.com/minecraft/mc-mods/simply-swords)
4. [Spartan Weaponry](https://www.curseforge.com/minecraft/mc-mods/spartan-weaponry)
5. [Spartan Shields](https://www.curseforge.com/minecraft/mc-mods/spartan-shields)

## Para probar pronto

Los mods que tengo que probar (para ver si funcionan) son:

1. [Towers of the Wild Modded](https://www.curseforge.com/minecraft/mc-mods/towers-of-the-wild-modded) -> Probar si es que es necesario tener instalado [Waystones](https://www.curseforge.com/minecraft/mc-mods/waystones), lo ideal sería tener únicamente TotW.
2. [Sound Physics](https://www.curseforge.com/minecraft/mc-mods/sound-physics-remastered) -> Probar sonido de salto
3. [Music Player](https://www.curseforge.com/minecraft/mc-mods/music-player) -> Revisar en el servidor
