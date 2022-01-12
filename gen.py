import random
import argparse

def gen_name(firstnames,lastnames,samples,FirstnameOnly):
    Out = []
    for i in range(1,samples):
        fid =  random.randint(1, len(firstnames)-1)
        lid =  random.randint(1, len(lastnames)-1)
        firstname = firstnames[fid].strip()
        if FirstnameOnly:
            FullName = firstname
            print(FullName)
            Out.append(FullName)
            continue
        else:
            lastname = lastnames[lid].strip()
            FullName = firstname + " " + lastname
            print(firstname + " " + lastname)
            Out.append(FullName)
    return Out

        
        
        


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a list of names')
    parser.add_argument('-s', '--samples', type=int, default=1, help='Number of samples to generate')
    parser.add_argument('-f', '--firstnames', type=str, default='firstnames.txt', help='First names file')
    parser.add_argument('-l', '--lastnames', type=str, default='lastnames.txt', help='Last names file')
    parser.add_argument('-o', '--output', type=str, default='names.txt', help='Output file')
    parser.add_argument('-F', '--firstnameonly',default=False, action='store_true', help='Only generate first names')
    # add argument to top names from file
    parser.add_argument('-t', '--top', type=int, default=0, help='Top names to use')
    args = parser.parse_args()

    firstnames = open(args.firstnames,'r').readlines()
    lastnames = open(args.lastnames,'r').readlines()


    if args.top > 0:
        firstnames = firstnames[:args.top]
        lastnames = lastnames[:args.top]      

    Names = gen_name(firstnames, lastnames, args.samples, args.firstnameonly)

    with open(args.output,'w') as f:
        for name in Names:
            f.write(name + '\n')
    print("Done")


