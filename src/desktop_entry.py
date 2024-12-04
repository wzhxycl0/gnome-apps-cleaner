class DesktopEntry:
    def __init__(self, fields):
        self.fields = fields

    def get_name(self):
        if 'name' in self.fields:
            return self.fields['name']
        return 'Unknown'

    def get_display(self):
        if 'display' in self.fields:
            return self.fields['display']
        return True

    def get_path(self):
        return self.fields['path']

    def set_display(self, value):
        self.fields['display'] = value

        with open(self.get_path(), 'r') as f:
            old_text = f.readlines()
            new_text = []

            for line in old_text:
                if not line.startswith('NoDisplay='):
                    new_text.append(line)

        with open(self.get_path(), 'w') as f:
            new_text.append(f'NoDisplay={value}')
            f.write('\n'.join(new_text))
