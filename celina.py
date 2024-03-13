import pandas
import math
teller = 0

def mijnmethode():
    pokemons = pandas.read_csv("Pokemon.csv")
    global teller
    teller += 1
    print(teller)
    print(pokemons)
    return "dit komt uit het bestand celina"

print (mijnmethode() + str(4+5))
# Create list of all programming languages without repeats
programming_languages = []
salary_survey = pandas.read_csv("IT_Salary_Survey_EU_2020.csv")
for i,regel in salary_survey.iterrows():
    new_entry= str(regel["Your main technology / programming language"])
    if new_entry.lower() in programming_languages:
        continue
    programming_languages.append(new_entry.lower())
print(programming_languages)
for x in programming_languages:
    print(x)

#Define for calculating average salaries for each programming language
def language_salary():
    salary_survey = pandas.read_csv("IT_Salary_Survey_EU_2020.csv")
    print(salary_survey)
    # Starting point for programming language salaries and user populations.
    python_totaal_salaris = 0
    python_aantal = 0
    js_totaal_salaris = 0
    js_aantal = 0
    java_totaal_salaris = 0
    java_aantal = 0
    sql_totaal_salaris = 0
    sql_aantal = 0
    ruby_totaal_salaris = 0
    ruby_aantal = 0
    csharp_totaal_salaris = 0
    csharp_aantal = 0
    php_totaal_salaris = 0
    php_aantal = 0
    cpp_totaal_salaris = 0
    cpp_aantal = 0
    kotlin_totaal_salaris = 0
    kotlin_aantal = 0
    es6_totaal_salaris = 0
    es6_aantal = 0
    scala_totaal_salaris = 0
    scala_aantal = 0
    vhdl_totaal_salaris = 0
    vhdl_aantal = 0
    swift_totaal_salaris = 0
    swift_aantal = 0
    ml_totaal_salaris = 0
    ml_aantal = 0
    yaml_totaal_salaris = 0
    yaml_aantal = 0
    c_totaal_salaris = 0
    c_aantal = 0
    embeddedc_totaal_salaris = 0
    embeddedc_aantal = 0
    objectivec_totaal_salaris = 0
    objectivec_aantal = 0
    r_totaal_salaris = 0
    r_aantal = 0
    bash_totaal_salaris = 0
    bash_aantal = 0
    pascal_totaal_salaris = 0
    pascal_aantal = 0
    elixir_totaal_salaris = 0
    elixir_aantal = 0
    erlang_totaal_salaris = 0
    erlang_aantal = 0
    abap_totaal_salaris = 0
    abap_aantal = 0
    qml_totaal_salaris = 0
    qml_aantal = 0
    groovy_totaal_salaris = 0
    groovy_aantal = 0
    cobol_totaal_salaris = 0
    cobol_aantal = 0
    clojure_totaal_salaris = 0
    clojure_aantal = 0
    julia_totaal_salaris = 0
    julia_aantal = 0
    perl_totaal_salaris = 0
    perl_aantal = 0
    haskell_totaal_salaris = 0
    haskell_aantal = 0
    sas_totaal_salaris = 0
    sas_aantal = 0
    matlab_totaal_salaris = 0
    matlab_aantal = 0
    ps_totaal_salaris = 0
    ps_aantal = 0
    css3_totaal_salaris = 0
    css3_aantal = 0
    ts_totaal_salaris = 0
    ts_aantal = 0
    go_totaal_salaris = 0
    go_aantal = 0
    vb_totaal_salaris = 0
    vb_aantal = 0
    spark_totaal_salaris = 0
    spark_aantal = 0
    # Calculations for average salaries of programming languages.
    for i,regel in salary_survey.iterrows():
        print("---",str(regel["Your main technology / programming language"]).lower())
        # Calculate average salary Python
        if "python" == str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            #for regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            python_aantal += 1
            python_totaal_salaris+=regel["Yearly brutto salary (without bonus and stocks) in EUR"]
        # Calculate average salary JavaScript
        elif "javascript" == str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            js_aantal += 1
            js_totaal_salaris+=regel["Yearly brutto salary (without bonus and stocks) in EUR"]
        elif "js" == str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            js_aantal += 1
            js_totaal_salaris+=regel["Yearly brutto salary (without bonus and stocks) in EUR"]
        # Calculate average salary Java
        elif "java" == str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            java_aantal += 1
            java_totaal_salaris+=regel["Yearly brutto salary (without bonus and stocks) in EUR"]
        # Calculate average salary SQL
        elif "sql" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            sql_aantal += 1
            sql_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
        # Calculate average salary Ruby
        elif "ruby" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            ruby_aantal += 1
            ruby_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
        # Calculate average salary C#
        elif "c#" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            csharp_aantal += 1
            csharp_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary PHP
        elif "php" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            php_aantal += 1
            php_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary C++
        elif "c++" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            cpp_aantal += 1
            cpp_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Kotlin
        elif "kotlin" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            kotlin_aantal += 1
            kotlin_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary ES6
        elif "es6" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            es6_aantal += 1
            es6_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Scala
        elif "scala" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            scala_aantal += 1
            scala_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary VHDL
        elif "vhdl" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            vhdl_aantal += 1
            vhdl_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Swift
        elif "swift" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            swift_aantal += 1
            swift_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary ML
        elif "ml" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            ml_aantal += 1
            ml_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary YAML
        elif "yaml" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            yaml_aantal += 1
            yaml_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary C
        elif "c" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            c_aantal += 1
            c_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Embedded C
        elif "embedded c" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            embeddedc_aantal += 1
            embeddedc_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Objective-C
        elif "objective-c" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            objectivec_aantal += 1
            objectivec_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary R
        elif "r" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            r_aantal += 1
            r_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Bash
        elif "bash" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            bash_aantal += 1
            bash_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Pascal
        elif "pascal" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            pascal_aantal += 1
            pascal_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Elixer
        elif "elixir" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            elixir_aantal += 1
            elixir_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Erlang
        elif "erlang" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            erlang_aantal += 1
            erlang_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary ABAP
        elif "abap" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            abap_aantal += 1
            abap_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary QML
        elif "qml" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            qml_aantal += 1
            qml_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Groovy
        elif "groovy" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            groovy_aantal += 1
            groovy_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Cobol
        elif "cobol" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            cobol_aantal += 1
            cobol_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Clojure
        elif "clojure" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            clojure_aantal += 1
            clojure_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Julia
        elif "julia" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            julia_aantal += 1
            julia_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Perl
        elif "perl" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            perl_aantal += 1
            perl_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Haskell
        elif "haskell" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            haskell_aantal += 1
            haskell_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary SAS
        elif "sas" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            sas_aantal += 1
            sas_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Matlab
        elif "matlab" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            matlab_aantal += 1
            matlab_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary PostScript
        elif "ps" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            ps_aantal += 1
            ps_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary CSS3
        elif "css3" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            css3_aantal += 1
            css3_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
          # Calculate average salary TypeScript
        elif "typescript" == str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            ts_aantal += 1
            ts_totaal_salaris+=regel["Yearly brutto salary (without bonus and stocks) in EUR"]
        elif "ts" == str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            ts_aantal += 1
            ts_totaal_salaris+=regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Go
        elif "go" == str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            go_aantal += 1
            go_totaal_salaris+=regel["Yearly brutto salary (without bonus and stocks) in EUR"]
        elif "golang" == str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            go_aantal += 1
            go_totaal_salaris+=regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Visual Basic
        elif "vb.net" == str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            vb_aantal += 1
            vb_totaal_salaris+=regel["Yearly brutto salary (without bonus and stocks) in EUR"]
        elif "vb" == str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            vb_aantal += 1
            vb_totaal_salaris+=regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            # Calculate average salary Spark
        elif "spark" == str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            spark_aantal += 1
            spark_totaal_salaris+=regel["Yearly brutto salary (without bonus and stocks) in EUR"]
        elif "apache spark" == str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            spark_aantal += 1
            spark_totaal_salaris+=regel["Yearly brutto salary (without bonus and stocks) in EUR"]
    print(python_aantal)
    print(python_totaal_salaris)
    print(python_totaal_salaris/python_aantal)
    print(js_aantal)
    print(js_totaal_salaris)
    print(js_totaal_salaris/js_aantal)
    print(java_totaal_salaris)
    print(java_totaal_salaris/js_aantal)
    print(sql_totaal_salaris)
    print(sql_totaal_salaris/js_aantal)
    print("ES6 INFO:")
    print(es6_aantal)
    print(es6_totaal_salaris)
    return "Average salary Python programmer in 2020: " + str(math.ceil(python_totaal_salaris/python_aantal)) + " EUR. Average salary JavaScript programmer in 2020: " + str(math.ceil(js_totaal_salaris/js_aantal)) + " EUR, average salary Java programmer in 2020: " + str(math.ceil(java_totaal_salaris/java_aantal)) + " EUR, average salary SQL programmer in 2020: " + str(math.ceil(sql_totaal_salaris/sql_aantal)) + " EUR, average salary Ruby programmer in 2020: " + str(math.ceil(ruby_totaal_salaris/ruby_aantal)) + " EUR, average salary C# programmer in 2020: " + str(math.ceil(csharp_totaal_salaris/csharp_aantal)) + " EUR, average salary PHP programmer in 2020: " + str(math.ceil(php_totaal_salaris/php_aantal)) + " EUR, average C++ programmer in 2020: " + str(math.ceil(cpp_totaal_salaris/cpp_aantal)) + " EUR, average Kotlin programmer in 2020: " + str(math.ceil(kotlin_totaal_salaris/kotlin_aantal)) + " EUR, average Go programmer in 2020: " + str(math.ceil(go_totaal_salaris/go_aantal)) + " EUR, average Scala programmer in 2020: " + str(math.ceil(scala_totaal_salaris/scala_aantal)) + " EUR, average VHDL programmer in 2020: " + str(math.ceil(vhdl_totaal_salaris/vhdl_aantal)) + " EUR, average Swift programmer in 2020: " + str(math.ceil(swift_totaal_salaris/swift_aantal)) + " EUR, average ML programmer in 2020: " + str(math.ceil(ml_totaal_salaris/ml_aantal)) + " EUR, average YAML programmer in 2020: " + str(math.ceil(yaml_totaal_salaris/yaml_aantal)) + " EUR, average C programmer in 2020: " + str(math.ceil(c_totaal_salaris/c_aantal)) + " EUR, average Objective-C programmer in 2020: " + str(math.ceil(objectivec_totaal_salaris/objectivec_aantal)) + " EUR, average R programmer in 2020: " + str(math.ceil(r_totaal_salaris/r_aantal)) + " EUR, average Bash programmer in 2020: " + str(math.ceil(bash_totaal_salaris/bash_aantal)) + " EUR, average Elixir programmer in 2020: " + str(math.ceil(elixir_totaal_salaris/elixir_aantal)) + " EUR, average Erlang programmer in 2020: " + str(math.ceil(erlang_totaal_salaris/erlang_aantal)) + " EUR, average ABAP programmer in 2020: " + str(math.ceil(abap_totaal_salaris/abap_aantal)) + " EUR, average QML programmer in 2020: " + str(math.ceil(qml_totaal_salaris/qml_aantal)) + " EUR, average Spark programmer in 2020: " + str(math.ceil(spark_totaal_salaris/spark_aantal)) + " EUR, average Cobol programmer in 2020: " + str(math.ceil(cobol_totaal_salaris/cobol_aantal)) + " EUR, average Clojure programmer in 2020: " + str(math.ceil(clojure_totaal_salaris/clojure_aantal)) + " EUR, average Julia programmer in 2020: " + str(math.ceil(julia_totaal_salaris/julia_aantal)) + " EUR, average Perl programmer in 2020: " + str(math.ceil(perl_totaal_salaris/perl_aantal)) + " EUR, average Haskell programmer in 2020: " + str(math.ceil(haskell_totaal_salaris/haskell_aantal)) + " EUR."

def language_name():
    language_survey = pandas.read_csv("IT_Salary_Survey_EU_2020.csv")
    for i,language in language_survey.iterrows():
        language["Your main technology / programming language"] = language["Your main technology / programming language"].str.lower()
        print(language)

def language_choice(de_taal):
    salary_survey = pandas.read_csv("IT_Salary_Survey_EU_2020.csv")
    for i,regel in salary_survey.iterrows():
        print("---",str(regel["Your main technology / programming language"]).lower())
        de_tekst_in_kleine_letters = str(regel["Your main technology / programming language"]).lower()
        if de_tekst_in_kleine_letters == de_taal :
            print("Yes, een match.")
        elif de_tekst_in_kleine_letters.find(de_taal) >= 0:
            print("Komt in de titel voor.")
    return "ABC" + de_taal