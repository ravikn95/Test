def split_and_join(line):
    line1=line.split(" ")
    line1="-".join(line1)
    return line1

    line=input()
    a=split_and_join(line)
