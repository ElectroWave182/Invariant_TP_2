def contient(t, x):

    for ele in t:
        if ele != x:
            return False
    return True


def drapeauM1(t):

    # Précondition
    n = len(t)
    assert n > 0, "Précondition : taille"
    for ele in t:
        assert ele in [0, 1], "Précondition : contenu"

    # Initialisation
    i = 0
    k = n - 1

    # Invariant
    assert len(t) == n, "Invariant pré-boucle : taille"
    assert 0 <= i <= k + 1 <= n, "Invariant pré-boucle : indices"
    assert contient(t[: i], 0), "Invariant pré-boucle : contenu 0"
    assert contient(t[k + 1 :], 1), "Invariant pré-boucle : contenu 1"

    # Boucle
    while i != k + 1:

        # Progression
        if t[i] == 1:
            t[i] = t[k]
            t[k] = 1
            k -= 1
        else:
            i += 1

        # Invariant
        assert len(t) == n, "Invariant boucle : taille"
        assert 0 <= i <= k + 1 <= n, "Invariant boucle : indices"
        assert contient(t[: i], 0), "Invariant boucle : contenu 0"
        assert contient(t[k + 1 :], 1), "Invariant boucle : contenu 1"
    
    # Postcondition
    assert i == k + 1, "Postcondition : pas de condition d'arrêt"

    # Invariant
    assert len(t) == n, "Invariant post-boucle : taille"
    assert 0 <= i <= k + 1 <= n, "Invariant post-boucle : indices"
    assert contient(t[: i], 0), "Invariant post-boucle : contenu 0"
    assert contient(t[k + 1 :], 1), "Invariant post-boucle : contenu 1"


# Tests

t1 = [1, 0, 0, 1, 0, 1, 1, 0]
drapeauM1(t1)
print(t1)

t2 = [0, 1, 1, 0, 1, 0, 0, 1]
drapeauM1(t2)
print(t2)

t3 = [0]
drapeauM1(t3)
print(t3)

t4 = [1]
drapeauM1(t4)
print(t4)

t5 = [1, 0, -1, 1]
drapeauM1(t5)
print(t5)

t6 = []
drapeauM1(t6)
print(t6)