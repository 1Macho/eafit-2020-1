# Conceptos básicos

## Ecuación diferencial

Es una ecuación donde interviene una función y una o más de sus derivadas.

$$
y'=y \rightarrow y=?
$$

La solución de una ecuación diferencial es una función que cumpla la ecuación.

$$
y=3l^x
$$

Notese que una ecuación diferencial puede tener infinitas soluciones, ya que es posible que, por ejemplo, los multiplos de una función tengan la misma derivada. 

$$
y=3l^x,y'=3l^x   \newline y=4l^x, y'=4l^x \newline ... \newline y=kl^x,y'=kl^x
$$

Las ecuaciones pueden ser ordinarias o parciales dependiendo de si las derivadas son con respecto a la misma variable o si son con respecto a varias variables, respectivamente. En este curso solo nos enfocaremos en las ordinarias.

También se clasifican dependiendo del orden y del grado. El orden es el grado de la más alta derivada que aparece en la ecuación. El grado es la potencia más alta a la que está elevada la derivada de mayor orden (siempre que la ecuación esté escrita en forma polinómica). 

Un concepto importante en las ecuaciones diferenciales es el de la linealidad o no linealidad. Una ecuación diferencial es lineal cuando la función y sus derivadas **no tienen exponente**.

$$
a_n(x)y^{(n)}+a_{n-1}(x)y^{(n-1)}+...+a_{1}(x)y'+a_0(x)y=h(x)
$$

Que también se puede escribir así cuando $F$ **es una función lineal**:

$$
F(x,y,y',...,y^{n})=0
$$

De esta forma, en algunos problemas es factible despejar la derivada de orden más alto, obteniendo

$$
y^{(n)}=G(x,y,y',...,y^{(n-1)})
$$

Notese que las ecuaciones diferenciales polinómicas no lineales repesentan varias ecuaciones diferenciales:

$$
y(y')^2-2xy'+y=0 \newline y'={{x+\sqrt{x^2-y^2}}\over{y}} , y'={{x-\sqrt{x^2-y^2}}\over{y}}
$$

## Ecuaciones de orden 1

$$
y'=f(x,y) \newline F(x,y,y')=0
$$

De las ecuaciones diferenciales podemos obtener información adicional acerca de la función. Por ejemplo:

$$
y''=y'=y
$$

Reconociendo que la primera derivada nos da la pendiente y la segunda derivada la concavidad, podemos ver que si $y$ es positiva, entonces $y$ es creciente y $y$ es concava hacia arriba. Similarmente, si $y$ es negativa, entonces $y$ es creciente y $y$ es concava hacia abajo. Todo esto sin saber con exactitud una solución para $y$.

## Problemas de valor inicial

Para que las ecuaciones diferenciales sean utiles, generalmente es necesario que estas tengan una única solución. Para que esto ocurra, deben existir condiciones adicionales que colapsen el conjunto de soluciones a una sola. 

Una forma de hacer esto es estableciendo un valor inicial para la función.

$$
xy'+y=0 \newline y(1)=1
$$

La solución en este caso se daría así:

$$
y'=-{{y}\over{x}} \newline xy=c \newline (1)(1)=c \newline c=1 \newline xy=1
$$

### Teorema de existencia y unicidad

Si $f(x,y)$ es continua y diferenciable cerca de un punto $(x_0,y_0)$ tal que $y(x_0)=y_0$ , entonces la ecuación diferencial ${{dy}\over{dx}}=f(x,y)$ tiene solución y es única. 

#### Ejemplo

$$
y'=x+y \newline y(0)=1
$$

¿Tiene solución única?

$$
f(x,y)=x+y
$$

Es continua en todo el plano (al estar compuesta de funciones lineales, no existen condiciones de continuidad). Cumple la primera condición de ser continua.

$$
{{\partial f}\over{\partial d}}=1
$$

Es continua y por lo tanto es diferenciable en todo el plano.

Por lo tanto, dado un valor inicial, existe una solución y es unica.

#### Ejemplo 2

$$
y'=\sqrt{1-x^2-y^2} \newline y(3)=4
$$

$$
f(x,y)=\sqrt{1-x^2-y^2}
$$

Es continua cuando $1-x^2-y^2>=0$.

Que puede analizarse mediante la forma $x^2+y^2=1$. Es decir, una circunferencia. 

Todo punto en su interior cumple la condición de ser continua.

Ahora es necesario analizar la derivada:

$$
{{\partial f}\over{\partial y}}={{-2y}\over{2\sqrt{1-x^2-y^2}}}
$$

En este caso la region diferenciable es el interior de la misma circunferencia mencionada anteriormente.

Ya que el punto $(3,4)$ está por fuera de la región continua y diferenciable, no existe una solución.

#### Problemas dificiles

Determinar si la función correspondiente representa una solución a la ecuación diferencial.

- $y'={{2xy}\over{x^2-y^2}}, cy=x^2+y^2$

- $y'=(2-y)(1-y),x=\ln{{2-y}\over{1-y}}$
