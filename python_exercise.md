### Python Exercise


#### Ex1_Walk


	import os

	def walk1(dirname):
    	for root, dirs, files in os.walk(dirname):
        	for file in files:
            	print os.path.join(root,file)

	def walk2(dirname):

    	for name in os.listdir(dirname):
        	path = os.path.join(dirname,name)
        	if os.path.isfile(path):
            	print path
        	else:
            	walk2(path)

	if __name__ == '__main__':
    	walk1('.')
    	walk2('.')



### Ex2_huiwen


	def find_huiwen(str):

    #for step in range(1,len(str)/2 +1):

    for step in range(len(str)/2 ,0, -1):

        for i in range(0, len(str)):

           

            if i+step*2+1 <= len(str):

                ls = list(str[i:i+step*2+1])

                if ls == ls[::-1]:

                    print str[i:i+step*2+1], i, step*2+1

                    return

               

            if i+step*2 <= len(str):

                ls = list(str[i:i+step*2])

                if ls == ls[::-1]:

                    print str[i:i+step*2], i, step*2

                    return



	if __name__ == '__main__':

    	test_str = raw_input("please input string>")

    	find_huiwen(test_str)
