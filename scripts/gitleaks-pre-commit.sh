#!/bin/bash
# Pre-commit hook: escanea archivos staged con Gitleaks
# Si detecta secrets, bloquea el commit y muestra dónde está el problema.
#
# Instalación:
#   1. Copiar a .githooks/pre-commit
#   2. git config core.hooksPath .githooks

if ! command -v gitleaks &> /dev/null; then
    echo "ADVERTENCIA: gitleaks no encontrado en PATH. Commit permitido sin escaneo."
    echo "  Instalar: winget install Gitleaks.Gitleaks  |  brew install gitleaks"
    exit 0
fi

# Escanear solo los archivos staged (--staged), no todo el repo
gitleaks git --staged --no-banner -v

EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    echo ""
    echo "=========================================="
    echo "  GITLEAKS: SECRET DETECTADO EN STAGING"
    echo "=========================================="
    echo ""
    echo "El commit fue BLOQUEADO porque se detectó"
    echo "un posible secret en los archivos staged."
    echo ""
    echo "Acciones:"
    echo "  1. Revisar el archivo y línea indicados arriba"
    echo "  2. Eliminar el secret del archivo"
    echo "  3. Si es un falso positivo, agregar excepción en .gitleaks.toml"
    echo "  4. Reintentar el commit"
    echo ""
    exit 1
fi
