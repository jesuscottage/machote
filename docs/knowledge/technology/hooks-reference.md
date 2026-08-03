---
title: Referencia de hooks opcionales
date: 2026-08-03
category: technology
tags: [hooks, gitleaks, seguridad, sonido, setup]
status: complete
---

# Referencia de hooks opcionales

> Referencia técnica para Claude. Contiene la configuración exacta de cada hook
> que se ofrece durante la inicialización del proyecto.

## 1. Sonido al terminar (Stop)

Emite 3 beeps ascendentes cuando Claude termina de responder.

```json
"Stop": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "powershell.exe -command \"[Console]::Beep(523,110); Start-Sleep -Milliseconds 40; [Console]::Beep(659,110); Start-Sleep -Milliseconds 40; [Console]::Beep(784,200)\" 2>/dev/null || true"
      }
    ]
  }
]
```

**Plataforma**: Windows (PowerShell). En macOS/Linux adaptar a `afplay`, `paplay` o `tput bel`.

## 2. Sonido de notificación (Notification)

Emite 2 beeps cortos cuando Claude pide permiso o envía una notificación.

```json
"Notification": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "powershell.exe -command \"[Console]::Beep(520,100); Start-Sleep -Milliseconds 80; [Console]::Beep(520,100)\" 2>/dev/null || true"
      }
    ]
  }
]
```

## 3. Pre-commit Gitleaks (detección de credenciales)

Escanea archivos staged antes de cada commit. Si encuentra API keys, tokens
o contraseñas, bloquea el commit.

### Archivos fuente

- `scripts/gitleaks-pre-commit.sh` — script del hook
- `scripts/gitleaks.toml` — configuración base de reglas

### Pasos de instalación

1. **Instalar el binario de Gitleaks**:
   ```bash
   # Windows
   winget install Gitleaks.Gitleaks

   # macOS
   brew install gitleaks

   # Linux (descargar release)
   # https://github.com/gitleaks/gitleaks/releases
   ```

2. **Crear directorio y copiar el hook**:
   ```bash
   mkdir -p .githooks
   cp scripts/gitleaks-pre-commit.sh .githooks/pre-commit
   chmod +x .githooks/pre-commit
   ```

3. **Copiar configuración a la raíz**:
   ```bash
   cp scripts/gitleaks.toml .gitleaks.toml
   ```

4. **Activar el directorio de hooks**:
   ```bash
   git config core.hooksPath .githooks
   ```

5. **Verificar**:
   ```bash
   gitleaks version          # Confirmar instalación
   git config core.hooksPath # Debe mostrar ".githooks"
   ```

### Notas

- El script permite el commit si Gitleaks no está instalado (con advertencia),
  así que no bloquea a colaboradores que no lo tengan.
- `.gitleaks.toml` se versiona con el repo — todos comparten las mismas reglas.
- `.githooks/` se versiona pero requiere `git config core.hooksPath` por colaborador.
- Agregar reglas personalizadas en `.gitleaks.toml` según el stack del proyecto.

---

## Flujo de instalación para Claude

Al ofrecer hooks durante el setup:

1. Presentar los 3 hooks con descripción de una línea
2. Preguntar cuáles desea activar
3. Para hooks de **sonido**: crear/actualizar `.claude/settings.json`
   - Si ya existe, hacer merge (no sobrescribir)
   - Si el usuario ya tiene los hooks en `~/.claude/settings.json` (global), informar que no es necesario duplicar
4. Para **Gitleaks**:
   - Verificar si `gitleaks` está instalado (`command -v gitleaks`)
   - Si está instalado: ejecutar los pasos 2-4 automáticamente
   - Si no está instalado: mostrar el comando de instalación según plataforma, pedir que lo instale, y luego continuar con pasos 2-4
   - Recordar que puede personalizar `.gitleaks.toml` con reglas de su stack
