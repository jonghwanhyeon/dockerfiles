#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <memory>
#include <sstream>
#include <string>
#include <vector>
#include <stdexcept>

#include <grp.h>
#include <pwd.h>
#include <unistd.h>

struct User {
  uid_t uid;
  gid_t gid;
  std::string login;
  std::string group;
  std::string home;
};

std::shared_ptr<User> find_user(const std::string& comment);
void run_as_root(const std::vector<std::string>& arguments);
std::string join(const std::vector<std::string>& items, const std::string& delimiter);

int main(void) {
  std::shared_ptr<User> previous_user = find_user("jonghwanhyeon/ml");

  User new_user = {getuid(),
                   getgid(),
                   previous_user->login,
                   previous_user->group,
                   previous_user->home};
  if (getenv("LOGIN_NAME") != nullptr) {
    std::string login = getenv("LOGIN_NAME");
    new_user.login = login;
    new_user.group = login;
    new_user.home = "/home/" + login;
  }

  try {
    run_as_root({
      "groupmod",
      "--gid", std::to_string(new_user.gid),
      previous_user->group});

    run_as_root({
      "usermod",
      "--uid", std::to_string(new_user.uid),
      "--gid", std::to_string(new_user.gid),
      "--login", new_user.login,
      "--home", new_user.home,
      "--move-home",
      previous_user->login});
  } catch (const std::runtime_error& error) {
    std::exit(1);
  }

  return 0;
}

std::shared_ptr<User> find_user(const std::string& comment) {
  struct passwd *entry = nullptr;

  setpwent();
  while((entry = getpwent()) != nullptr) {
    if (entry->pw_gecos == comment) {
      struct group *group = getgrgid(entry->pw_gid);
      return std::shared_ptr<User>(new User {entry->pw_uid,
                                             entry->pw_gid,
                                             entry->pw_name,
                                             group->gr_name,
                                             entry->pw_dir});
    }
  }
  endpwent();

  return nullptr;
}

#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunused-result"
void run_as_root(const std::vector<std::string>& arguments) {
  uid_t current_uid = getuid();

  setreuid(0, -1);
  int result = std::system(join(arguments, " ").c_str());
  setreuid(current_uid, -1);

  if (result != 0) {
    throw std::runtime_error("return code is non-zero");
  }
}
#pragma GCC diagnostic pop

std::string join(const std::vector<std::string>& items, const std::string& delimiter) {
  if (items.empty()) {
    return "";
  }

  std::stringstream stream;
  for (const auto& item : items) {
    stream << item << delimiter;
  }

  std::string joined = stream.str();
  return joined.substr(0, joined.size() - delimiter.size());
}
