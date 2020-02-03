# Fundamentos conjuntistas

## Conjunto universal

$$
U=\{ X: X \in A \vee X \notin A \}
$$

$$
\phi = \{ X: X \in A \wedge X \notin A \}
$$

## Unión e intersección

$$
A \cup B = \{ X: X \in A \vee X \in B \}
$$

$$
A \cap B = \{ X: X \in A \wedge X \in B \}
$$

## Subconjuntos

$$
A \subset B = \{ X \in A \rightarrow X \in B \}
$$

De esto se deduce que:

- $A \subset A \cup B$

- $A \cap B \subset A$

## Conjuntos disyuntos y exhaustivos

- Disyuntos: No tienen elementos comunes. $A \cap B = \phi$

- Exhaustivos: Al unirlos, resulta el todo. $A \cup B = U$

## Complemento

$$
\bar A = \{ X: X \notin A \}
$$

## Diferencia

$$
A - B = \{ X: X \in A \wedge X \notin B \}
$$

$$
A-B = A \cap \bar B
$$

## Secuencia de conjuntos a secuencia de conjuntos disyuntos.

Sea $A$ tal que $\cup_{n=1}^{\inf} A _n=S$. Es posible construir un conjunto $B$ tal que $B_n \cap B_m = \phi, n \ne m$ y $\cup_{i=1}^{\inf} B_i = S$.

Esto se logra al definir $B_n=A_n-\cup_{i=1}^{n-1}A_i$.
