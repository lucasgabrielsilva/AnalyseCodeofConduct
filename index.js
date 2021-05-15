const { format } = require('@fast-csv/format');
const path = require("path");
const fs = require("fs");
const csv = require('@fast-csv/parse');
const { Octokit } = require("@octokit/core");

const octokit = new Octokit({ auth: `` });

const csvHeader = [
    'owner',
    'name',
    'createdAt',
    'language',
    'url',
    'stargauzers',
    'description'
];

const languages = [
   "JavaScript", 
    "Python", 
    "Java", 
    "TypeScript", 
    "C#", 
    "C", 
    "cpp", 
    "PHP", 
    "Ruby", 
    "Go", 
    "Kotlin", 
    "Swift", 
    "Objective-C", 
    "Julia", 
    "R", 
    "Scala", 
    "Rust", 
    "Perl", 
    "Clojure", 
    "MATLAB"   
];

const pages = [1, 2, 3, 4, 5];

let csvWrite = [];
csvWrite.push(csvHeader);


const saveCsv = (data) => {
    const ws = fs.createWriteStream('/home/pexe/utf/MR/minering/bases/base1.csv');
    const stream = format({ headers: true, delimiter: '\t' });
    stream.pipe(ws);
    stream.write(data[0]);
    data.shift();
    data.forEach(page => {
        page.forEach(row => {
            stream.write(row)
        })
    });
    stream.end();
}


const minering = async () => {

    aux = await Promise.all(languages.map(async (language) => {
        csvWrite.push(await Promise.all(pages.map(async (page) => {
            return await getRepoData(page, language)
        }))); 
        return csvWrite;
    }));
    console.log(csvWrite.length)
    let aux2 = [csvWrite[0]];
    await Promise.all(csvWrite[1].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[2].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[3].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[4].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[5].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[6].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[7].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[8].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[9].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[10].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[11].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[12].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[13].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[14].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[15].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[16].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[17].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[18].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[19].map((page) => {
        aux2.push(page)
        return page;
    }));
    await Promise.all(csvWrite[20].map((page) => {
        aux2.push(page)
        return page;
    }));
    saveCsv(aux2)
}


const getRepoData = async (page, language) => {
    const response = await octokit.request('GET /search/repositories', {
        q: `language:${language}`,
        sort:"stars",
        order: "desc",
        per_page: 100,
        page:page
    })

    let toCsv = [];
    let aux = [];
    toCsv.push(await Promise.all(response.data.items.map((repo) => {
        aux = [
            repo.owner.login,
            repo.name,
            repo.created_at,
            repo.language,
            repo.html_url,
            repo.stargazers_count,
            repo.description

        ];
        return aux;
    })));
    return toCsv[0]



};

minering();

