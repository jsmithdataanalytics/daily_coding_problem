
class Content:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'


class File(Content):

    def get_max_path(self):
        return self.name


class Directory(Content):

    def __init__(self, name, contents):
        super().__init__(name)
        self.contents = []

        while contents:
            content_name = contents.pop(0)

            if 'dir' in content_name:
                content_contents = []

                while contents and contents[0][0] == '\t':
                    content_contents.append(contents.pop(0)[1:])

                content = Directory(content_name, content_contents)

            else:
                content = File(content_name)

            self.contents.append(content)

    def get_max_path(self):
        longest = ''

        for obj in self.contents:
            candidate = obj.get_max_path()
            candidate = f'{self.name}/{candidate}' if candidate else ''

            if len(candidate) > len(longest):
                longest = candidate

        return longest


class Filesystem:

    def __init__(self, string):
        self.root = Directory(name='', contents=string.split('\n'))

    def get_max_file_path(self):
        return self.root.get_max_path()[1:]

    def get_length_of_longest_file_path(self):
        return len(self.get_max_file_path())


if __name__ == '__main__':
    example = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'

    assert Filesystem(example).get_length_of_longest_file_path() == 32
    assert Filesystem('dir\n\tsubdir1\n\tsubdir2').get_length_of_longest_file_path() == 0
