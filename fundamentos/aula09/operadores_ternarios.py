esta_chovendo = True

# Sem if
clima = 'Hoje está ' + ('Sol.', 'Chovendo.')[esta_chovendo]
print(clima)

# Com if
clima = 'Hoje está ' + ('Chovendo.' if esta_chovendo else 'Sol.')
print(clima)
