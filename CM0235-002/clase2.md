# Métodos de solución

## Método de separación de variables

$$
f(x,y)={{h(x)}\over{g(y)}}=h(x)g(y)
$$

Separar la función original en dos funciones que dependan exclusivamente de X y Y.

$$
{{dy}\over{dx}}={{h(x)}\over{g(y)}} \newline g(y)dy=h(x)dx \newline \int g(y)dy=\int h(x)dx
$$

En algunos casos no es posible separar la ecuación original en dos funciones, pero es posible hacerlo al realizar transformaciones y cambios de variable.

### Funciones homogeneas

$f(x,y)$ es homogénea de grado $n$ si

$$
f(tx,ty)=t^nf(x,y)
$$

Ejemplo

$$
f(x,y)=x^2+3xy+y^2 \newline
f(tx,ty)=(tx)^2+3(tx)(ty)+(ty)^2 \newline
=t^2x^2+3t^2xy+t^2y^2 \newline
=t^2(x^2+3xy+y^2) =t^2f(x,y)
$$

Es homogenea de grado 2.

Si se puede escribir como $f(y/x)$ donde $g=g(u)$ es una función de una sola variable, entonces puede resolverse en términos de $u$.

### Ejemplos - Sección 1.2.2

#### 4

$$
(1-\cos \theta) dr = r \sin \theta d \theta \newline
{{dr}\over{r}}={{\sin\theta}\over{1-\cos\theta}}d\theta \newline
\int{{dr}\over{r}}=\int{{\sin\theta d \theta} \over {1-cos\theta}} \newline
\ln r = \ln (1-\cos \theta)+C \text{ [Solución implicita]} \newline
\ln r - \ln (1-\cos \theta) = C \newline 
\ln \left({{r} \over {1-\cos \theta}} \right) =C \newline
{{r}\over{1-\cos \theta}}=e ^ {c} \newline 
{{r}\over{1-\cos\theta}}=A \newline
r=A(1-\cos \theta)
$$

#### 32

$$
{{dy}\over{dx}}={{x-y-3}\over{x+y-1}}
$$


