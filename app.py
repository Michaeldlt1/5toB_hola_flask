from flask import Flask, render_template_string

app = Flask(__name__)

# CSS Puro integrado directamente para evitar bloqueos del navegador
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Sitio Flask</title>
    <style>
        /* Estilos Base */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f8fafc;
            color: #334155;
            display: flex;
            flex-direction: column;
            min-h-screen: 100vh;
            height: 100vh;
        }

        /* Barra de Navegación */
        nav {
            background-color: #ffffff;
            border-bottom: 1px solid #e2e8f0;
            padding: 1rem 2rem;
        }
        .nav-container {
            max-width: 1000px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .logo {
            font-size: 1.25rem;
            font-weight: bold;
            color: #4f46e5;
        }
        .nav-links a {
            color: #64748b;
            text-decoration: none;
            margin-left: 1.5rem;
            transition: color 0.2s;
        }
        .nav-links a:hover {
            color: #4f46e5;
        }

        /* Contenido Principal */
        main {
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 2rem;
            max-width: 800px;
            margin: 0 auto;
        }
        .badge {
            background-color: #e0e7ff;
            color: #4338ca;
            font-size: 0.875rem;
            font-weight: 600;
            padding: 0.25rem 0.75rem;
            border-radius: 50px;
            margin-bottom: 1.5rem;
            display: inline-block;
        }
        h1 {
            font-size: 3rem;
            font-weight: 800;
            color: #0f172a;
            line-height: 1.2;
            margin-bottom: 1rem;
        }
        h1 span {
            color: #4f46e5;
        }
        p {
            font-size: 1.125rem;
            color: #64748b;
            margin-bottom: 2rem;
            max-width: 600px;
        }

        /* Botones */
        .btn-group {
            display: flex;
            gap: 1rem;
        }
        .btn-primary {
            background-color: #4f46e5;
            color: #ffffff;
            padding: 0.75rem 1.5rem;
            border-radius: 0.5rem;
            text-decoration: none;
            font-weight: 500;
            transition: background-color 0.2s;
        }
        .btn-primary:hover {
            background-color: #4338ca;
        }
        .btn-secondary {
            background-color: #ffffff;
            color: #475569;
            padding: 0.75rem 1.5rem;
            border-radius: 0.5rem;
            text-decoration: none;
            font-weight: 500;
            border: 1px solid #cbd5e1;
            transition: background-color 0.2s;
        }
        .btn-secondary:hover {
            background-color: #f8fafc;
        }

        /* Pie de Página */
        footer {
            background-color: #ffffff;
            border-top: 1px solid #e2e8f0;
            padding: 1.5rem;
            text-align: center;
            font-size: 0.875rem;
            color: #94a3b8;
        }
    </style>
</head>
<body>

    <nav>
        <div class="nav-container">
            <span class="logo">Flask🎯</span>
            <div class="nav-links">
                <a href="#">Inicio</a>
                <a href="#">Servicios</a>
                <a href="#">Contacto</a>
            </div>
        </div>
    </nav>

    <main>
        <span class="badge">¡Servidor Activo!</span>
        <h1>Una página bonita en <span>Flask</span></h1>
        <p>Este sitio web se está ejecutando completamente desde un único archivo Python con CSS nativo y está escuchando a través del puerto 6000.</p>
        
        <div class="btn-group">
            <a href="http://127.0.0.1:6000" class="btn-primary">Actualizar Página</a>
            <a href="https://palletsprojects.com" target="_blank" class="btn-secondary">Documentación</a>
        </div>
    </main>

    <footer>
        <p>&copy; 2026 Desarrollado con Flask y Python.</p>
    </footer>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
