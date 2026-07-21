import json

# Base de datos pre-configurada con IDs estables en español que admiten incrustación completa sin trabas
biblioteca_estable = [
    {
        "titulo": "El Principito",
        "autor": "Antoine de Saint-Exupéry",
        "id_archive": "elprincipito0000sain",
        "portada": "https://covers.openlibrary.org/b/id/14515518-M.jpg"
    },
    {
        "titulo": "Narrativa Completa Vol. 1",
        "autor": "H.P. Lovecraft",
        "id_archive": "narrativacomplet0001love",
        "portada": "https://covers.openlibrary.org/b/id/8302521-M.jpg"
    },
    {
        "titulo": "Narrativa Completa Vol. 2",
        "autor": "H.P. Lovecraft",
        "id_archive": "narrativacomplet0002love",
        "portada": "https://covers.openlibrary.org/b/id/12642531-M.jpg"
    },
    {
        "titulo": "Cuentos Completos",
        "autor": "Edgar Allan Poe",
        "id_archive": "cuentoscompletos0000poee",
        "portada": "https://covers.openlibrary.org/b/id/10555306-M.jpg"
    },
    {
        "titulo": "Drácula",
        "autor": "Bram Stoker",
        "id_archive": "dracula0000stok_u4u0",
        "portada": "https://covers.openlibrary.org/b/id/14515456-M.jpg"
    },
    {
        "titulo": "Cincuenta Sombras de Grey",
        "autor": "E. L. James",
        "id_archive": "cincuentasombra0000jame",
        "portada": "https://covers.openlibrary.org/b/id/12833591-M.jpg"
    },
    {
        "titulo": "Misterios",
        "autor": "H.P. Lovecraft",
        "id_archive": "misterios0000love",
        "portada": "https://covers.openlibrary.org/b/id/8232930-M.jpg"
    }
]

with open("libros.json", "w", encoding="utf-8") as f:
    json.dump(biblioteca_estable, f, ensure_ascii=False, indent=2)

print("¡Archivo 'libros.json' generado con éxito con enlaces estables en español!")