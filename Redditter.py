#!/usr/bin/python3
import argparse

def table(text, align="left"):
    with open(text, "r") as f:
        header = next(f)
        rows = list()
        lines = f.readlines()
        for l in lines:
            rows.append(l)
    header = header.replace(",","|")
    header = header.replace("\"", "")
    count = 1
    for h in header:
        if h == "|":
            count += 1
    
    print("{}".format(header))
    
    if align == "left":
        al = ":--|"*count
        al = al [:-1]
        print("{}".format(al))    
    elif align == "center":
        al = ":-:|"*count
        al = al [:-1]
        print("{}".format(al))
    elif align == "right":
        al = "--:|"*count
        al = al [:-1]
        print("{}".format(al))   
    for r in rows:
        r = r.replace(",","|")
        r = r.replace("\"","")
        print(r)
     
def hover_text(args):
    text = args[0]
    link = args[1]    
    if len(args) == 2:
        link_text = text
    else:
        link_text = args[2]
    print("[{0}]({1} \"{2}\")".format(text,link,link_text))

def spoiler_text(args):
    print("[{}](#s \"{}\")".format(args[0],args[1]))

def header_text(args):
    if int(args[1]) > 6:
        size = 6
    else:
        size = int(args[1])
    header = args[0]
    print("{}{}".format("#"*size,header))

        

def main():
    parser = argparse.ArgumentParser()

    #Setting up parser arguments
    parser.add_argument("-s","--spoiler", nargs=2,type=str,
            help="Prints out formatted spoiler text, with the second argument as the shown text")
    parser.add_argument("-H","--header", nargs=2,
            help="Prints out header text, header as first argument and size as second argument")
    parser.add_argument("-t","--table",
            help="Creates a table of the provided file, first line is header next are rows.")
    parser.add_argument("-a","--align", type=str,
            help="Used with --table to align, \"left\",\"center\",\"right\" ")
    parser.add_argument("-O","--hover",nargs=3, type=str,
            help="Outputs text formatted as hover text, the first argument is the text, the second argument the link and the third argument the hover text")
    args = parser.parse_args()
    
    if type(args.spoiler) != type(None):
        spoiler_text(args.spoiler)
    elif type(args.header) != type(None):
        header_text(args.header)
    elif type(args.table) != type(None):
        if type(args.align) != type(None):
            table(args.table, align=args.align)
        else:
            table(args.table)
    elif type(args.hover) != type(None):
        hover_text(args.hover)
    return 0

if __name__ == "__main__":
    main()

