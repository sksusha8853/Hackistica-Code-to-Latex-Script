from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
# from textblob import TextBlob

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyse', methods=['POST'])
def analyse():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        received_text=rawtext
        rawtext=request.form['rawtext'].split("\n")
        print(type(rawtext))
        
        a = rawtext

    # n = int(input())
    # for i in range(0,n):
    #     b=input()
    #     a.append(b)
  
    
        final_ans = []
    
        # Starting latex lines
        final_ans.append("\\documentclass{article}")
        final_ans.append("\\usepackage[utf8]{inputenc}")
        final_ans.append("\\usepackage{algorithm}")
        final_ans.append("\\usepackage{algpseudocode}")
        final_ans.append("\n")
        final_ans.append("\\title{hackistica}")
        final_ans.append("\\author{cse200001043 }")
        final_ans.append("\\date{January 2023}")
        final_ans.append("\n")
        final_ans.append("\\begin{document}")
        final_ans.append("\\maketitle")
        final_ans.append("\n")
        final_ans.append("\n")
        final_ans.append("\\begin{algorithm}")
    
    
        # Removing empty spaces from lines
        for i in range(0,len(a)):
            a[i] = a[i].strip()
        
        
        # Extracting useless lines before function name like blank lines and comments
        while len(a)>0:
            
            # Removing blank lines
            if(len(a[0])==0):
                a.pop(0)
                
            else:
                
                if(len(a[0])>=2):
                    
                    # Removing single line comments
                    if(a[0][0]=='/' and a[0][1]=='/'):
                        strin = ""
                        a[0] = a[0][2:]
                        a[0] = a[0].strip()
                        strin += a[0]
                        strin = strin.strip()
                        strin = "\\Comment{" + strin + "}"
                        final_ans.append(strin)
                        a.pop(0)
                        
                    else:
                        
                        # Removing multiple line comments
                        if(a[0][0]=='/' and a[0][1]=='*'):
                            strin = ""
                    
                            # Removing multiple line comments that appear on single line
                            if(len(a[0])>=4 and a[0][-2]=='*' and a[0][-1]=='/'):
                                a[0] = a[0][2:-2]
                                a[0] = a[0].strip()
                                strin += a[0]
                                strin += " "
                                a.pop(0)
                                
                            # Removing multiple line comments that appear on different multiple line
                            else:
                                a[0] = a[0][2:]
                                a[0] = a[0].strip()
                                strin += a[0]
                                strin += " "
                                a.pop(0)
                                
                                while(len(a)>0):
                                
                                    if(len(a[0])>=2):
                                        if(a[0][-2]=='*' and a[0][-1]=='/'):
                                            a[0] = a[0][0:-2]
                                            a[0] = a[0].strip()
                                            strin += a[0]
                                            strin += " "
                                            a.pop(0)
                                            break
                                        else:
                                            a[0] = a[0].strip()
                                            strin += a[0]
                                            strin += " "
                                            a.pop(0)
                                            
                                    else:
                                        a.pop(0)
                            
                            strin = strin.strip()
                            strin = "\\Comment{" + strin + "}"
                            final_ans.append(strin)
                            
                        else:
                            break
                        
                else:
                    break
        
        
    
        # Extracting function from code
        function_name = ""
        index = 0 
        for i in range(0,len(a[0])):
            if(a[0][i]=='('):
                index=i 
                break
            
        function_name = a[0][:index]
        function_name = function_name.strip()
        a[0] = a[0][index:]
        
        index = 0
        for i in range(len(function_name)-1,-1,-1):
            if(function_name[i]==' '):
                index = i 
                break
        
        function_name = function_name[index+1:]
        
        function_name1 = "\\Procedure{" + function_name +"}{"
        function_name = "\\caption{" + function_name + "}"
        
        final_ans.append(function_name)
        final_ans.append("\\begin{algorithmic}")
        
        
        
        
        
        # Extracting function parameters from code
        a[0] = a[0][1:]
        func_parameters = ""

        while len(a)>0:
            index = 0

            a[0] = a[0].strip()
            if(len(a[0])==0):
                continue

            for i in range(0,len(a[0])):
                if(a[0][i]==',' or a[0][i]==')'):
                    index = i
                    break
        
            parame = a[0][:index]
            a[0] = a[0][index:]

            parame = parame.strip()
        
            for i in range(len(parame)-1,-1,-1):
                if(parame[i]==' '):
                    index = i
                    break
            
            parame = parame[index+1:]
            if(parame[0]=='&'):
                parame = parame[1:]
            
            parame = parame + ","

            func_parameters = func_parameters + parame




            if(a[0][0]==')'):
                a[0] = a[0][1:]
                break
            else:
                a[0] = a[0][1:]


        func_parameters = func_parameters[:-1]
        function_name1 = function_name1 + func_parameters + "}"
        final_ans.append(function_name1)

        a[0] = a[0].strip()

        if(len(a)>0 and len(a[0])>=2):
            if(a[0][0]=='/' and a[0][1]=='/'):
                a[0] = a[0][2:]
                a[0] = a[0].strip()
                strin = ""
                strin = "\\Comment{" + a[0] + "}"
                final_ans.append(strin)
                a.pop(0)

        if(len(a)>0 and len(a[0])>=4):
            if(a[0][0]=='/' and a[0][1]==''  and a[0][-2]=='' and a[0][-1]=='/'):
                a[0] = a[0][2:-2]
                a[0] = a[0].strip()
                strin = ""
                strin = "\\Comment{" + a[0] + "}"
                final_ans.append(strin)
                a.pop(0)
        final_ans.append("\\end{algorithmic}")
        final_ans.append("\\end{algorithm}")
        final_ans.append("\n")
        final_ans.append("\\end{document}")
    
        for x in a:
            print(x)
        for x in final_ans:
            print(x)
        
        print(rawtext)
        message=final_ans
        
    
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
