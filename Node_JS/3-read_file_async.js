const fs = require('fs').promises;

function countStudents(path) {
    return fs.readFile(path, 'utf-8')
        .then((content) => {
            const lines = content.split('\n').filter((line) => line.trim() !== '');
            if (lines.length <= 1) {
                console.log('Number of students: 0');
                return;
            }

            const students = lines.slice(1)
            .map((line) => line.split(','))
            .filter((columns) => columns.length <= 4 && columns[3].trim() !== '')
            .map((columns) => ({
                firstName: columns[0].trim(),
                field: columns[3].trim()
            }));
            
            const fields = {};
            students.forEach((student) => {
                if(!fields[student.field]) {
                fields[student.field] = [];
                }
                fields[student.field].push(student.firstName);
            });

            console.log(`Number of students: ${students.length}`);
            for (const [field, names] of Object.entries(fields)) {
                console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
            }
        })
        .catch(() => {
            throw new Error('Cannot load the database');
        });
}

module.exports = countStudents;
