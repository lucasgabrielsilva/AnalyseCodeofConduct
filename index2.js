const { format } = require('@fast-csv/format');
const csv = require('@fast-csv/parse');
const path = require("path");
const fs = require("fs");
const { Octokit } = require("@octokit/rest");

const octokit = new Octokit({ auth: `` });

tocsv = [['hasCode', 'code', 'url']];
toElse = [['Owner', 'Name']];
sucess = 0;
fails = 0;

const saveCsv = () => {
    const ws = fs.createWriteStream('/home/pexe/utf/MR/minering/bases/base2.csv');
    const stream = format({ headers: true, delimiter: '\t' });
    stream.pipe(ws);
    stream.write(tocsv[0]);
    tocsv.shift();
    tocsv.forEach(row => {
        stream.write(row)
    })
    stream.end();
    console.log('Sucess: ', sucess, 'fail: ', fails);
}

const saveCsv2 = () => {
    const ws = fs.createWriteStream('/home/pexe/utf/MR/minering/errors/errorsElse.csv');
    const stream = format({ headers: true, delimiter: '\t' });
    stream.pipe(ws);
    stream.write(toElse[0]);
    toElse.shift();
    toElse.forEach(row => {
        stream.write(row)
    })
    stream.end();
}


const intervalo = async (element) => {
    try {
        let response = await octokit.rest.codesOfConduct.getForRepo({
            owner: element.owner,
            repo: element.name,
        });
        if(response.data.body){
            let aux = ['Yes', `${element.owner}-_-${element.name}.txt`, response.data.html_url]
            tocsv.push(aux);
            sucess += 1;
            fs.writeFileSync(`/home/pexe/utf/MR/minering/codesOfConduct/${element.language}/${element.owner}-_-${element.name}.txt`, response.data.body);
            console.log(`${tocsv.length} - ${element.name} - Sucess`);
        }
        else{
            let aux = ['No', 'null', 'null']
            tocsv.push(aux);
            fails += 1;
            toElse.push([element.owner, element.name]);
            console.log(`${tocsv.length} - ${element.name} - Fail: else`);
        }
    } catch (err){
        let aux = ['No', 'null', 'null']
        tocsv.push(aux);
        fails += 1;
        fs.writeFileSync(`/home/pexe/utf/MR/minering/errors/${element.owner}-_-${element.name}.txt`, err.toString());
        console.log(`${tocsv.length} - ${element.name} - Fail: Catch`);
    }
}


const getCodeCoduct = async (data) => {

    let pos = 0;
    const inter = setInterval(async () => {
        intervalo(data[pos]);
        pos += 1;
        if(pos == data.length){
            setTimeout(() => {
                clearInterval(inter)
                saveCsv()
                saveCsv2();
            }, 1300);
        }
    }, 1500);
}

const readCsv = () => {
    const path = "/home/pexe/utf/MR/minering/bases/base1.csv";
    let data = [];
    csv.parseFile(path, {headers: true, delimiter: ',' })
        .on('error', error => console.error(error))
        .on('data', (row) => {
            data.push(row)
        }).on('end', () => {
            getCodeCoduct(data)
        });
}

readCsv();
