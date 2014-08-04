__author__ = 'sivins'

"""Your calculator must be able to convert between metres, inches, miles and attoparsecs.
It must also be able to convert between kilograms, pounds, ounces and hogsheads of Beryllium."""

print 'Acceptable units for distance: metres, inches, miles, attoparsecs'
print 'Acceptable units for weight: kilograms, pounds, ounces, hogsheads of Beryllium'
n = raw_input("How many:")
oldUnits = raw_input("Old units:")
newUnits = raw_input('New Units:')
print 'Converting %s %s to %s' % (n, oldUnits, newUnits)

table = {
    'metres' : {
        'inches' : 39.3701,
        'miles' : 0.000621371,
        'attoparsecs' : 32.4077929
},
    'inches' : {
        'metres' : 0.0254,
        'miles' : 1.5783e-5,
        'attoparsecs' : 0.82315794
},
    'miles' : {
        'inches' : 63360,
        'metres' : 1609.34,
        'attoparsecs' : 52155.287
},
    'attoparsecs' : {
        'inches' : 1.21483369,
        'metres' : 0.0308567758,
        'miles' : 1.91735116e-5
}
}

conversion = table[oldUnits][newUnits]

nNew = float(n)*conversion

print '%s %s is equal to %s %s' % (n, oldUnits, nNew, newUnits)