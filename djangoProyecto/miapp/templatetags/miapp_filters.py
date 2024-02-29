from django import template

register = template.Library()


@register.filter(name='saludo')
def saludo(value):
    largo=''
    if len(value)>=8:
        largo='<p>Tu nombre es muy largo explorador</p>'
    return f'<h1 style="background:green;color:white;">Bienvenido explorador, {value} </h1>'+largo

@register.filter(name='numUnidades')
def numUnidades(value):
    try:
        numUnidades = int(value)
        return f'Hay {value} unidades de peluches en la tienda.'
    except ValueError:
        return 'Imposible valor de unidades, el valor proporcionado no es un número.'

@register.filter(name='mayusculas')
def mayusculas(value):
    return value.upper()

@register.filter(name='precioP')
def precioP(value):
    precio = {
        'nami': 'Valor de: $50.000',
        'yuumi': 'Valor de: $75.000',
        'escurridizo': 'Valor de: $68.900',

    }
    return f'Articulo {mayusculas(value)}: '+precio.get(value, 'Valor desconocido')

@register.filter(name='habilidades')
def habilidades(value):
    habilidades = {
        'Irelia': [
            'Q: Irelia se lanza hacia un objetivo, infligiendo daño y aplicando efectos adicionales.',
            'W: Irelia se prepara para un contraataque, reduciendo el daño recibido y aumentando su daño básico.',
            'E: Irelia lanza un proyectil que aturde al primer enemigo golpeado.',
            'R: Irelia lanza una ráfaga de cuchillas que infligen daño a los enemigos y curan a Irelia si golpean a campeones.',
        ],
        'Yuumi': [
            'Q: Yuumi lanza un misil mágico que inflige daño a los enemigos y marca a los campeones aliados.',
            'W: Yuumi se une a un campeón aliado, otorgándole bonificaciones y la capacidad de lanzar habilidades.',
            'E: Yuumi cura a un campeón aliado y le otorga un escudo.',
            'R: Yuumi lanza un rayo que inflige daño a los enemigos y cura a los campeones aliados.',
        ],
        'Teemo': [
            'Q: Teemo envenena a un enemigo, infligiendo daño adicional durante un período de tiempo.',
            'W: Teemo se vuelve invisible y aumenta su velocidad de movimiento.',
            'E: Teemo coloca una trampa que inflige daño y envenena a los enemigos que la activan.',
            'R: Teemo lanza una serie de hongos venenosos que infligen daño a los enemigos y los ralentizan.',
        ],
        'Senna': [
            'Q: Senna dispara una ráfaga de energía que inflige daño a los enemigos y cura a los aliados.',
            'W: Senna lanza una niebla que ralentiza a los enemigos y les inflige daño si están enraizados.',
            'E: Senna se camufla y se mueve más rápido.',
            'R: Senna dispara un rayo que inflige daño a los enemigos y cura a los aliados.',
        ],
        'Jax': [
            'Q: Jax se lanza hacia un objetivo, infligiendo daño y aplicando efectos adicionales.',
            'W: Jax golpea al suelo con su arma, infligiendo daño a los enemigos cercanos.',
            'E: Jax se defiende de los ataques básicos y reduce el daño recibido.',
            'R: Jax se vuelve más fuerte, aumentando su daño de ataque y su resistencia mágica.',
        ],
        # Agrega más campeones y sus habilidades aquí
    }
    return habilidades.get(value, ['Not found'])

@register.filter(name='categorias')
def categorias(value):
    categorias = {
        'Lacteos': [
            'Leche',
            'Queso',
            'Mantequilla',
        ],
        'Verduras':[
            'Apio',
            'Cebolla',
            'Acelga',
        ],
        'Carnes':[
            'Res',
            'Cerdo',
            'Pollo',
        ],
        'Aseo':[
            'Limpido',
            'Jabon',
            'Shampoo',
        ]
    }
    return categorias.get(value, ['Not found'])