with open("C:/Users/Stuti Shah/Downloads/rpm_unique_without_version_ognb.txt") as remp_file:
    rpm_ognb_list = [line.strip()for line in remp_file]
print(rpm_ognb_list)

with open("C:/Users/Stuti Shah/Downloads/rpm_unique_without_version_ccdu.txt") as ccdu_file:
    rpm_ccdu_list = [line.strip()for line in ccdu_file]
print(rpm_ccdu_list)

package_list_differance = []
for packages in rpm_ccdu_list:
    if packages not in rpm_ognb_list:
        package_list_differance.append(packages)
print(package_list_differance)

file_path = "C:/Users/Stuti Shah/Downloads/package_differance.txt"

with open (file_path,"w") as file:
    data_to_write = "\n".join(package_list_differance)
    file.write(data_to_write)
print(f"the list has been written to {file_path}. ")