#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class SteuerIdentChecker(object):

	def __init__(self,identNumber):
		self.identNumber = identNumber
		
	def checkChecksum(self):
		product = 10
		for i in range(0,10):
			sum = (int(self.identNumber[i]) + product) % 10
			if (sum == 0):
				sum = 10
			product = (sum * 2) % 11
		checkNum = 11 - product
		if (checkNum == 10):
			checkNum = 0
		if checkNum == int(self.identNumber[10]):
			print "Prüfziffer stimmt überein! Ihre Nummer scheint richtig!"
			return True
		else:
			print "Prüfziffer stimmt nicht überein! Ihre Nummer scheint falsch!"
			print "FEHLER: Ihre Prüfziffer ist " + self.identNumber[10] + " und die errechnete Prüfziffer ist " + str(checkNum)
			return False
			
	def checkForNull(self):
		if int(self.identNumber[0]) == 0:
			print "FEHLER: Die Identifikationsnummer darf nicht mit 0 beginnen!"
			return False
		else:
			return True
	
	def checkNumNumbers(self):
		hasNoNumber = False
		for i in range(0,9):
			if self.identNumber[0:10].count(str(i)) == 0:
				 hasNoNumber = True
				 noNumber = i
				 break
		if hasNoNumber == False:
			print "FEHLER: Die Identifikationsnummer enthält alle Ziffern von 0 bis 9!"
		hasTwoNumber = False
		for i in range(0,9):
			if self.identNumber[0:10].count(str(i)) == 2:
				 hasTwoNumber = True
				 twoNumber = i
				 break
		if hasTwoNumber == False:
			print "FEHLER: Die Identifikationsnummer enthält keine Zahl genau zweimal!"
		otherNumOne = True
		for i in range(0,9):
			if self.identNumber[0:10].count(str(i)) != 1 and i != noNumber and i != twoNumber:
				otherNumOne = False
				break
		if otherNumOne == False:
			print "FEHLER: Alle anderen Zahlen dürfen nur einmal vorkommen!"
		
			
			
print "Bitte geben Sie ihre Steuerliche Identifikationsnummer ein:"
eingabe = raw_input("> ")


checker = SteuerIdentChecker(eingabe)
checker.checkChecksum()
checker.checkForNull()
checker.checkNumNumbers()
