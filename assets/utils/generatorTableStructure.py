print("<table>")

full_path = "\"assets/images/case_1/generator_results"
groups = 12

group_count = 0
open_tr = True
for i in range(0, 2000, 100):
    if open_tr:
        print("\t<tr>")
        open_tr = False

    print("\t\t<td>", end="")
    print("<img src={0}/image_at_epoch_{1:05d}_00000.png\" alt=\"\">".format(full_path, i), end="")
    print("</td>")

    group_count += 1
    if group_count % groups == 0:
        print("\t</tr>")
        open_tr = True

for i in range(2000, 231000, 1000):
    if open_tr:
        print("\t<tr>")
        open_tr = False

    print("\t\t<td>", end="")
    print("<img src={0}/image_at_epoch_{1:05d}_00000.png\" alt=\"\">".format(full_path, i), end="")
    print("</td>")

    group_count += 1
    if group_count % groups == 0:
        print("\t</tr>")
        open_tr = True

if not open_tr:
    print("\t</tr>")

print("</table>")
