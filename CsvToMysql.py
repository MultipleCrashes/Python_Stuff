import csv 
import MySQLdb
import os


#chaneg self.csv_filename to the csv file name
class CsvMysqlDump:
	def __init__(self):
		#pwd by default
		self.csv_path = os.path.dirname(os.path.abspath(__file__))
		self.csv_filename = 'breakup.csv'
 
	def csv_to_mysqldb(self,csv_path=None,csv_filename=None):
		if csv_path:
			self.csv_path = csv_path
		if csv_filename:
			self.csv_filename = csv_filename	
		with open(self.csv_path+os.sep+self.csv_filename,'r') \
							   as data_file:
			for line in data_file:
				line = line.strip('\r\n') 
				line = line.split(",")
				print "Line ->",line


if __name__ == '__main__':
	obj= CsvMysqlDump()
	obj.csv_to_mysqldb()
