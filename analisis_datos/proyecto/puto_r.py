import pandas as pd


data = pd.read_csv('./Resultados_de_An_lisis_de_Laboratorio_Suelos_en_Colombia.csv')
var_list = ['Departamento', 'Municipio', 'Cultivo', 'Topografia', 'Drenaje',
          'Riego', 'pH.agua.suelo.2.5.1.0', 'Materia.orgánica..MO...',
          'Fósforo..P..Bray.II.mg.kg', 'Azufre..S..Fosfato.monocalcico.mg.kg',
          'Acidez..Al.H..KCL.cmol....kg', 'Aluminio..Al..intercambiable.cmol....kg',
          'Calcio..Ca..intercambiable.cmol....kg', 'Magnesio..Mg..intercambiable.cmol....kg',
          'Potasio..K..intercambiable.cmol....kg', 'Sodio..Na..intercambiable.cmol....kg',
          'capacidad.de.intercambio.cationico..CICE..suma.de.bases.cmol....kg',
          'Conductividad.el.ctrica..CE..relacion.2.5.1.0.dS.m', 'Hierro..Fe..disponible.olsen.mg.kg',
          'Cobre..Cu..disponible.mg.kg', 'Manganeso..Mn..disponible.Olsen.mg.kg',
          'Zinc..Zn..disponible.Olsen.mg.kg', 'Boro..B..disponible.mg.kg', 
          'Hierro..Fe..disponible.doble..cido.mg.kg', 'Cobre..Cu..disponible.doble.acido.mg.kg',
          'Manganeso..Mn..disponible.doble.acido.mg.kg', 'Zinc..Zn..disponible.doble..cido.mg.kg']

data = data[var_list]

print(data.head())
