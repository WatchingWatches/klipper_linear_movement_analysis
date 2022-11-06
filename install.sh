#!/bin/bash
if [ "$EUID" == 0 ]
  then echo "This script is not intended to be run as user root"
  exit 1
fi

EXTENSION_TARGET="${HOME}/klipper/klippy/extras"
SCRIPT_NAME="linear_movement_vibrations.py"

function link_extension_file{
    if [ -d "${EXTENSION_TARGET}" ]; then
        rm -f "${EXTENSION_TARGET}/${SCRIPT_NAME}"
        ln -sf ${SCRIPT_NAME} "${KLIPPY_EXTRAS}/${SCRIPT_NAME}"
    else
        echo -e "${EXTENSION_TARGET} not found, exiting installation."
        exit 1
    fi

}


echo -e "Installation Script for Klipper Linear Movement Analysis by MarschallMarc#6420"
echo -e "Linking extension file"
link_extension_file
# exits on error but works, so dont check
~/klippy-env/bin/pip install -v matplotlib
