def changecase(func):
  def myinner():
    return func().upper()
  return myinner

if __name__ == "__main__":
    print ("Formatowanie is being run directly")

    @changecase
    def napisz():
        text = "Ala ma kota"
        return text
    print(napisz())


else:
    print ("Formatowanie is being imported")