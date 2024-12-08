with open('input') as f:
    input_lines = f.read().strip().splitlines()

targets, vals_list = zip(*[line.split(":") for line in input_lines])
targets = list(map(int, targets))
vals_list = list(list(map(int, v.strip().split())) for v in vals_list)

def find_op_sequence(target, vals):
    n = len(vals)
    if n==1:
        return vals[0]==target
    else:
        d,r = divmod(target, vals[-1])
        if r==0:
            res = find_op_sequence(d, vals[:-1])
            if res:
                return True
        diff = target-vals[-1]
        if diff >= 0 and find_op_sequence(diff, vals[:-1]):
            return True

        # comment for part 1; include for part 2
        val_str = str(vals[-1])
        target_str = str(target)
        if len(val_str) < len(target_str) and target_str[-len(val_str):] == val_str:
            return find_op_sequence(int(target_str[:-len(val_str)]), vals[:-1])

        return False


print(sum(targets[i] for i in range(len(targets)) if find_op_sequence(targets[i],vals_list[i])))