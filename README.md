# Casa en Orden

Curso en el celular para ordenar y limpiar la casa. Este repositorio publica solo:

- **Página de venta** (`index.html`) en GitHub Pages.
- **App Android** (`CasaEnOrden.apk`) compilada sola en cada cambio y subida a *Releases*.

## Cambiar precio, link de pago o WhatsApp
Editá `config.json` (desde el celular, con el lápiz de GitHub) y guardá. En unos minutos se actualizan la página y la app.

## Secretos (Settings > Secrets and variables > Actions)
- `CLAVE_CODIGOS`: clave con la que se calculan los códigos de activación.
- `KEYSTORE_PEM`: clave con la que se firma la app (para poder actualizarla sin desinstalar).

No los pongas nunca en archivos del repositorio.
