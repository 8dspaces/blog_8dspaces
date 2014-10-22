# coding: utf8
import random 

def main():

    shenghui = {
            "shanxi":"taiyuan", "shandong":"jinan",
            "jiangsu":"nanjing", "zhejiang":"hangzhou",
    }
    
    welcome = """
    ================================
    you will become a simple testing
            Good luck!!
    ================================
    """
    print welcome

    wrong_answer = []
    while len(shenghui):
    
        random_test = random.choice(shenghui.keys())
        correct_answer = shenghui[random_test]
        your_answer = raw_input("which is shenghui of %s" % random_test)
        
        if your_answer.strip().lower() == correct_answer:
            print "correct, good one"
            del shenghui[random_test]
        else:
            print "wrong, think more"
            wrong_answer.append(your_answer.strip().lower())
            
    if wrong_answer:
        print "you need read more books!"
    else:
        print "perfect, play more^_^"
    
    
if __name__ == "__main__":
    print __file__
    main()