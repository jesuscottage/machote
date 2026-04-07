# User-Level Hooks Setup / Configuración de Hooks de Usuario

These hooks are configured **once per machine** in `~/.claude/settings.json`.
They are NOT project-specific — they apply to ALL Claude Code sessions.

## What these hooks do

| Hook | When it fires | What it does |
|------|--------------|-------------|
| `Stop` | When Claude finishes a task | Plays a 3-tone ascending chime (C-E-G) |
| `Notification` | When Claude needs your attention | Plays a double beep |

## Configuration by OS

### Windows (PowerShell)

Add to `~/.claude/settings.json`:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "powershell.exe -command \"[Console]::Beep(523,110); Start-Sleep -Milliseconds 40; [Console]::Beep(659,110); Start-Sleep -Milliseconds 40; [Console]::Beep(784,200)\" 2>/dev/null || true"
          }
        ]
      }
    ],
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
  },
  "effortLevel": "high"
}
```

### macOS

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "afplay /System/Library/Sounds/Glass.aiff 2>/dev/null || true"
          }
        ]
      }
    ],
    "Notification": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "afplay /System/Library/Sounds/Pop.aiff 2>/dev/null || true"
          }
        ]
      }
    ]
  },
  "effortLevel": "high"
}
```

### Linux

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "paplay /usr/share/sounds/freedesktop/stereo/complete.oga 2>/dev/null || beep -f 523 -l 110 -D 40 -f 659 -l 110 -D 40 -f 784 -l 200 2>/dev/null || true"
          }
        ]
      }
    ],
    "Notification": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "paplay /usr/share/sounds/freedesktop/stereo/message.oga 2>/dev/null || beep -f 520 -l 100 -D 80 -f 520 -l 100 2>/dev/null || true"
          }
        ]
      }
    ]
  },
  "effortLevel": "high"
}
```

## Additional settings

| Setting | Value | Description |
|---------|-------|-------------|
| `effortLevel` | `"high"` | Claude puts more effort into responses |

## How to apply

1. Open or create `~/.claude/settings.json`
2. Copy the JSON block for your OS
3. If the file already exists, **merge** the hooks (don't overwrite other settings)
4. Restart Claude Code for changes to take effect

## Asking Claude to configure

You can also ask Claude to configure these for you:

```
Configure the notification hooks from the machote's setup/setup-hooks.md
in my ~/.claude/settings.json
```

Claude will detect your OS and apply the correct version.
