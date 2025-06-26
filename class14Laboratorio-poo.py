class libro:
  def __init__(self, Titulo, Autor, isbn, paginas):
      self.Titulo = Titulo
      self.Autor = Autor
      self.isbn = isbn
      self.paginas = paginas
      self.leido = False
      self.paginas_leidas = 0
      self.porcentaje_leido = 0.0
      self.fecha_lectura = None

  def __str__(self):
      return f"Libro: {self.Titulo}, Autor: {self.Autor}, ISBN: {self.isbn}, Páginas: {self.paginas}, Leído: {self.leido}, Páginas leídas: {self.paginas_leidas}, Porcentaje leído: {self.porcentaje_leido}, Fecha de lectura: {self.fecha_lectura}"
      
      #return f"Libro: {self.Titulo}, Autor: {self.Autor}, ISBN: {self.isbn}, Páginas: {self.paginas}, Leído: {self.leido}, Páginas leídas: {self.paginas_leidas}, Porcentaje leído: {self.porcentaje_leido}, Fecha de lectura: {self.fecha_lectura}"
      #return f"Libro: {self.Titulo}, Autor: {self.Autor}, ISBN: {self.isbn}, Páginas: {self.paginas}, Leído: {self.leido}, Páginas le
      #idas: {self.paginas_leidas}, Porcentaje leído: {self.porcentaje_leido}, Fecha de lectura: {self.fecha_lectura}"


