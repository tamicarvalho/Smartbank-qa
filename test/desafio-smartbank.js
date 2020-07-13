var should = require('should')
var axios = require('axios')
var logger = require('mocha-logger')
var chai = require('chai')
var expect = chai.expect
var baseUrl = 'http://dummy.restapiexample.com/api/v1'
var id = ''

describe('Desafio #1 - SmartBank - Criar Empregado', function() {

    var api = ''
    it('Dado que eu tenha a API de criação de empregado', function() {
        api = baseUrl + '/create'
    })

    var response = {}
    it('Quando eu criar um empregado', async function() {
        var requestBody = {
            name: 'test', 
            salary: '123', 
            age: '23'
        }
        response = await axios.post(api, requestBody)
    })

    var data = {}
    it('Então eu devo validar a resposta da API', function() {
        expect(response.status).to.equal(200)
        var body = response.data
        expect(body.should.have.property('data'))
        data = body.data
        expect(data.should.have.property('id'))
    })

    it('E guardar o ID gerado', function() {
        id = data.id
        expect(id).exist
        logger.log('ID gerado para o empregado:', id)
    })
})

describe('Desafio #1 - SmartBank - Buscar Empregado', function() {

    var api = ''
    it('Dado que eu tenha a API de busca de empregado', function() {
        api = baseUrl + '/employee/' + id
    })

    var response = {}
    it('Quando eu buscar o empregado criado', async function() {
        expect(id).exist
        response = await axios.get(api)
        logger.log('Buscando o empregado com o ID:', id)
    })

    it('Então eu devo validar a resposta da API', function() {
        expect(response.status).to.equal(200)
        // var body = response.data
        // expect(body.should.have.property('status'))
        // expect(body.should.have.property('data'))
        // expect(body.status).to.equal('success')
        // expect(body.data.id).to.equal(id)
    })
})

describe('Desafio #1 - SmartBank - Remover Empregado', function() {

    var api = {}
    it('Dado que eu tenha a API de remoção de empregado', function() {
        api = baseUrl + '/delete/' + id
    })

    var response = {}
    it('Quando eu remover o empregado criado', async function() {
        expect(id).exist
        response = await axios.delete(api)
        logger.log('Removendo o empregado com o ID:', id)
    })

    it('Então eu devo validar a resposta da API', function() {
        expect(response.status).to.equal(200)
        var body = response.data
        expect(body.should.have.property('status'))
        expect(body.should.have.property('message'))
        // expect(body.status).to.equal('success')
        // expect(body.message).to.equal('successfully! deleted Records')
    })
})