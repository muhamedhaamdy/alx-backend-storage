# NoSQL Database Class

Welcome to the NoSQL Database Class repository. This repository contains notes, code examples, and resources related to the NoSQL class.

## Table of Contents

1. [Introduction to NoSQL](#introduction-to-nosql)
2. [SQL vs NoSQL](#sql-vs-nosql)
3. [ACID Properties](#acid-properties)
4. [Document Storage](#document-storage)
5. [Types of NoSQL Databases](#types-of-nosql-databases)
6. [Benefits of NoSQL Databases](#benefits-of-nosql-databases)
7. [Querying in NoSQL Databases](#querying-in-nosql-databases)
8. [CRUD Operations in NoSQL Databases](#crud-operations-in-nosql-databases)
9. [Working with MongoDB](#working-with-mongodb)

## Introduction to NoSQL

NoSQL stands for "Not Only SQL." It encompasses a wide variety of database technologies that were developed in response to the demands of modern software applications. NoSQL databases are designed to handle large volumes of data, provide flexible data models, and scale horizontally.

## SQL vs NoSQL

### SQL Databases
- Relational databases
- Use structured query language (SQL)
- Predefined schema
- Vertical scalability

### NoSQL Databases
- Non-relational databases
- Flexible schema
- Horizontal scalability
- Various data models: document, key-value, wide-column, graph

## ACID Properties

ACID is a set of properties that guarantee reliable transaction processing in SQL databases:

- **Atomicity**: Transactions are all-or-nothing.
- **Consistency**: Transactions move the database from one valid state to another.
- **Isolation**: Concurrent transactions do not interfere with each other.
- **Durability**: Once a transaction is committed, it remains so.

## Document Storage

Document storage is a type of NoSQL database that stores data in document formats like JSON, BSON, or XML. Each document is a self-contained unit and can contain nested structures.

## Types of NoSQL Databases

1. **Document Databases**: MongoDB, CouchDB
2. **Key-Value Stores**: Redis, DynamoDB
3. **Wide-Column Stores**: Cassandra, HBase
4. **Graph Databases**: Neo4j, OrientDB

## Benefits of NoSQL Databases

- **Scalability**: Easy horizontal scaling
- **Flexibility**: Schema-less data models
- **Performance**: Optimized for specific use cases
- **Big Data**: Handle large volumes of data efficiently

## Querying in NoSQL Databases

Each NoSQL database has its own query mechanism:

- **MongoDB**: Query language similar to JSON
- **Redis**: Key-based commands
- **Cassandra**: Cassandra Query Language (CQL), similar to SQL

## CRUD Operations in NoSQL Databases

Examples of basic CRUD operations in different NoSQL databases:

### MongoDB
```javascript
// Insert
db.collection.insertOne({ name: "John", age: 30 });

// Query
db.collection.find({ name: "John" });

// Update
db.collection.updateOne({ name: "John" }, { $set: { age: 31 } });

// Delete
db.collection.deleteOne({ name: "John" });

