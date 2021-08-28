import sys
import getopt

def print_usage():
#	print('python3 argv.py -u <username> -p <password>')
#	print('python3 argv.py --username <username> --password <password>')

	print('python argv.py OPTIONS')
	print('OPTIONS')
	print('{:>6} {:<20}{}'.format('-c', '--channel', 'Channel id of the Youtuve channel to download'))
	print('{:>6} {:<20}{}'.format('', '--cleanup', 'Remove captions and videos downloaded during run'))


def main():
	print(sys.argv[1:])

	short_opts = 'hu:p:' #有接:(冒號)就是要輸入參數
	long_opts = 'help username= password= clearup'.split() #會切成一個清單
	try:
		opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
	except getopt.GetoptError:
		print_usage()
		sys.exit(2)
	
	username = ''
	password = ''
#	print(opts)
#	print(args)
	for opt, arg in opts:
		if opt == '-h':
			print_usage()
			sys.exit(0)
		elif opt in ("-u", "--username"):
			username = arg
		elif opt in ("-p", "--password"):
			password == arg
		#elif opt == 'clearup'


	if not username or not password:
		print_usage()
	#	sys.exit(2)
#	print(username)
#	print(password)

if __name__ == '__main__':
	main()


